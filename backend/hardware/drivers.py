import time
import threading
from hardware.connection import find_arduino
from utils.logger import logger


class DriversArduino:
    def __init__(self, baudrate=500000):
        self.arduino = find_arduino('ok', 'drivers', baudrate)
        if self.arduino:
            self.arduino.reset_input_buffer()

        self.lock = threading.Lock()
        self.events = {
            'ok': threading.Event(),
            'MOVED': threading.Event(),
            'started': threading.Event(),
            'stopped': threading.Event()
        }

        self.response_actions = {
            'OK': lambda: self._set_flag('ok'),
            'MOVED': lambda: self._set_flag('MOVED'),
            's_start': lambda: self._set_flag('started'),
            's_stop': lambda: self._set_flag('stopped'),
            's1': lambda: self._set_flag('MOVED'),
            'is_stopping_s1_finished': lambda: self._set_flag('stopped'),
        }

        self.stop_thread = False
        self.read_thread = threading.Thread(target=self._reader_loop, daemon=True)
        self.read_thread.start()

    def _send_wait(self, cmd: str, wait_for: str, timeout: float = 1.0):
        with self.lock:
            if wait_for in self.events:
                self.events[wait_for].clear()

            self._write(cmd)

            if wait_for in self.events:
                success = self.events[wait_for].wait(timeout)
                if not success:
                    logger.error(f"Timeout waiting for '{wait_for}' (Cmd: {cmd})")

    def _set_flag(self, name):
        if name in self.events:
            self.events[name].set()

    def set_manual_speed(self, rpm: float):
        val = int(rpm)
        self._write(f"{10000 + val}")

    def set_rpm(self, rpm: float):
        val = int(rpm)
        self._write(f"{20000 + val}")

    def set_width(self, mm: float):
        val = int(mm * 10)
        self._write(f"{70000 + val}")

    def set_diameter(self, mm: float):
        val = int(mm * 100)
        self._write(f"{80000 + val}")

    def move_manual(self, steps: int):
        if steps == 0: return
        cmd = f"{30000 + steps}" if steps > 0 else f"{40000 + abs(steps)}"
        self._send_wait(cmd, 'MOVED', timeout=5.0)

    def start_winding(self):
        self._send_wait("59999", 'started', timeout=2.0)

    def stop_winding(self):
        self._send_wait("69999", 'stopped', timeout=5.0)

    def _write(self, data):
        if self.arduino:
            try:
                msg = f"{data}\n".encode('utf-8')
                self.arduino.write(msg)
                self.arduino.flush()
                time.sleep(0.05)
            except Exception as e:
                logger.error(f"Serial write error: {e}")

    def _reader_loop(self):
        while not self.stop_thread:
            if self.arduino and self.arduino.in_waiting:
                try:
                    line = self.arduino.readline().decode().strip()
                    if line in self.response_actions:
                        self.response_actions[line]()
                except Exception:
                    pass
            time.sleep(0.001)