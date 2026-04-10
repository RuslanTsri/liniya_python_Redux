import threading
import time


from config import *
from utils.logger import logger


class PinManager:
    def __init__(self):
        self._pin_modes = {}
        self._callbacks = []

    def setup_pin(self, pin: int, mode: str):
        if mode.upper() == 'IN':
            GPIO.setup(pin, GPIO.IN)
            self._pin_modes[pin] = 'IN'
        elif mode.upper() == 'OUT':
            GPIO.setup(pin, GPIO.OUT)
            self._pin_modes[pin] = 'OUT'
        else:
            raise ValueError(f"Invalid mode: {mode}")

    def read(self, pin: int) -> bool:
        return GPIO.input(pin) == GPIO.HIGH

    def write(self, pin: int, value: bool):
        if self._pin_modes.get(pin) != 'OUT':
            raise RuntimeError(f"Pin {pin} is not set as OUTPUT")
        GPIO.output(pin, GPIO.HIGH if value else GPIO.LOW)

    def add_callback(self, pin: int, value: bool, func):
        self._callbacks.append({'pin': pin, 'value': value, 'func': func, 'handled': False})

    def get_callbacks(self):
        return self._callbacks


class Detector:
    def __init__(self, press_hold_time=0.1, poll_interval=0.01):
        self.press_hold_time = press_hold_time
        self.poll_interval = poll_interval
        self._running = True

        self.is_change_right_set_enable = False
        self.is_change_left_set_enable = False

        self.start_callback = None
        self.stop_callback = None

        self.gpio = PinManager()

        self._initialize_gpio()
        self._register_internal_callbacks()
        self._start_monitor_thread()

    # ------------------- PUBLIC API -------------------

    def bip(self, count, delay):
        for _ in range(count):
            GPIO.output(BIP_PIN, 1)
            time.sleep(1 * delay / 1000)
            GPIO.output(BIP_PIN, 0)
            time.sleep(0.5 * delay / 1000)

    def set_start_callback(self, func):
        self.start_callback = func

    def set_stop_callback(self, func):
        self.stop_callback = func

    def is_change_right_en(self):
        if IS_CHANGE_RIGHT_DISABLED:
            return False
        if IS_FAKE_CHANGE_DETECTORS:
            return self.is_change_right_set_enable
        return self._is_pin_active(CHANGE_RIGHT_PIN, CHANGE_RIGHT_EN_STATE)

    def is_change_left_en(self):
        if IS_FAKE_CHANGE_DETECTORS:
            return self.is_change_left_set_enable
        return self._is_pin_active(CHANGE_LEFT_PIN, CHANGE_LEFT_EN_STATE)

    def cleanup(self):
        self._running = False
        self._monitor_thread.join()

    def init_input_pin(self, pin: int):
        self.gpio.setup_pin(pin, 'IN')

    def init_output_pin(self, pin: int):
        self.gpio.setup_pin(pin, 'OUT')

    def read_pin(self, pin: int) -> bool:
        return self.gpio.read(pin)

    def output_pin(self, pin: int, value: bool):
        self.gpio.write(pin, value)

    def add_callback_to_pin(self, pin: int, value: bool, func):
        self.gpio.add_callback(pin, value, func)

    # ------------------- INIT -------------------

    def _initialize_gpio(self):
        GPIO.setmode(GPIO.BOARD)
        self._setup_input_pins()

    def _setup_input_pins(self):
        self.init_input_pin(RUN_BTN_PIN)
        self.init_input_pin(STOP_BTN_PIN)
        self.init_input_pin(CHANGE_RIGHT_PIN)
        self.init_input_pin(CHANGE_LEFT_PIN)
        self.init_output_pin(BIP_PIN)

    def _register_internal_callbacks(self):
        self.add_callback_to_pin(RUN_BTN_PIN, RUN_BTN_EN_STATE, self._on_run_pressed)
        self.add_callback_to_pin(STOP_BTN_PIN, STOP_BTN_EN_STATE, self._on_stop_pressed)

    def _start_monitor_thread(self):
        thread = threading.Thread(target=self._monitor_loop, daemon=True)
        thread.start()
        self._monitor_thread = thread

    # ------------------- MONITORING -------------------

    def _monitor_loop(self):
        while self._running:
            self._check_custom_pins()

            if IS_FAKE_CHANGE_DETECTORS:
                self._check_fake_change_right()
                self._check_fake_change_left()

            time.sleep(self.poll_interval)

    # ------------------- UNIVERSAL PIN CALLBACK HANDLER -------------------

    def _check_custom_pins(self):
        for cb in self.gpio.get_callbacks():
            pin = cb['pin']
            expected_value = cb['value']
            func = cb['func']
            handled = cb.get('handled', False)

            a = 0
            for _ in range(10):
                a += 1 if GPIO.input(pin) == expected_value else 0
                time.sleep(0.01)

            is_active = True if a >= 7 else False

            if is_active:
                if not handled and self._is_signal_stable(pin, expected_value):
                    threading.Thread(target=func, daemon=True).start()
                    cb['handled'] = True
            else:
                cb['handled'] = False

    # ------------------- CALLBACK HANDLERS -------------------

    def _on_run_pressed(self):
        logger.info("run button pressed (held)")
        if self.start_callback:
            self.start_callback()

    def _on_stop_pressed(self):
        logger.info("stop button pressed (held)")
        if self.stop_callback:
            self.stop_callback()

    # ------------------- FAKE DETECTORS -------------------

    def _check_fake_change_right(self):
        state = GPIO.input(CHANGE_RIGHT_PIN)
        if self._has_fake_change_right_toggled(state):
            self._toggle_fake_change_right()

    def _check_fake_change_left(self):
        state = GPIO.input(CHANGE_LEFT_PIN)
        if self._has_fake_change_left_toggled(state):
            self._toggle_fake_change_left()

    def _has_fake_change_right_toggled(self, state):
        return state != self.is_change_right_set_enable and \
            self._is_signal_stable(CHANGE_RIGHT_PIN, state)

    def _has_fake_change_left_toggled(self, state):
        return state != self.is_change_left_set_enable and \
            self._is_signal_stable(CHANGE_LEFT_PIN, state)

    def _toggle_fake_change_right(self):
        self.is_change_right_set_enable = not self.is_change_right_set_enable
        logger.debug(f'is_change1_set_enable: {self.is_change_right_set_enable}')

    def _toggle_fake_change_left(self):
        self.is_change_left_set_enable = not self.is_change_left_set_enable
        logger.debug(f'is_change2_set_enable: {self.is_change_left_set_enable}')

    # ------------------- SIGNAL CHECKING -------------------

    def _is_pin_active(self, pin, active_state):
        for _ in range(10):
            if not GPIO.input(pin) is active_state:
                return False
            time.sleep(0.001)

        return True

    def _is_signal_stable(self, pin, expected_state):
        start_time = time.time()
        while time.time() - start_time < self.press_hold_time:
            if GPIO.input(pin) != expected_state:
                return False
            time.sleep(self.poll_interval)
        return True


# ------------------- USAGE EXAMPLE -------------------

detector = Detector()

if __name__ == '__main__':
    def custom_start():
        print("Custom START logic")


    def custom_stop():
        print("Custom STOP logic")


    # detector.set_start_callback(custom_start)
    # detector.set_stop_callback(custom_stop)

    try:
        while True:
            if detector.is_change_right_en():
                print("Change RIGHT detected!")

            if detector.is_change_left_en():
                print("Change LEFT detected!")

            time.sleep(0.5)

    except KeyboardInterrupt:
        print("Exiting test...")
        detector.cleanup()
