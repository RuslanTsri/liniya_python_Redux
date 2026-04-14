import time
import threading
from utils.logger import logger
from hardware.detectors import detector
from core.settings import config
from config import RPM_UP_K, BIP_COUNT, BIP_DELAY, LOW_COMPENSATION_LIMIT, HIGH_COMPENSATION_LIMIT


class WindingProcess:
    # ОТРИМУЄ ЗАЛІЗО ВІД MAIN.PY
    def __init__(self, steppers, encoders):
        self.steppers = steppers
        self.encoders = encoders

        self.is_parking = False
        self.is_filament_winding = False
        self.is_bip = False
        self.finished_filament_meters = 0.0
        self._meters_left_to_bip = 100
        self._prev_rpm = 0

        detector.set_start_callback(self.start_filament_winding)
        detector.set_stop_callback(self.stop_filament_winding)

    def setup_filament_winding(self):
        self.reset_winding_state()
        self.is_filament_winding = True

    def start_filament_winding(self):
        if self.is_filament_winding or self.is_parking:
            return

        self.setup_filament_winding()
        self.steppers.start_full_sync(config.spool_width, config.filament_thickness)

        threading.Thread(target=self._loop_safety_monitor, daemon=True).start()
        threading.Thread(target=self._loop_meters, daemon=True).start()
        threading.Thread(target=self._loop_compensation, daemon=True).start()

    def stop_filament_winding(self):
        if not self.is_filament_winding: return
        logger.info('stop winding')
        self.is_filament_winding = False
        self.steppers.stop_sync()

    def park_carriege(self, _=None, is_force=False):
        if self.is_parking and not is_force: return
        logger.info('parking')
        self.is_parking = True

        self.stop_filament_winding()
        time.sleep(0.5)
        self.steppers.homing()
        self.reset_winding_state()
        logger.info('stop parking')
        self.is_parking = False

    def motors_rpm_compensation(self):
        encoder_value = self.encoders.get_compensation_encoder_value()
        target_rpm = config.user_spool_rpm

        if 0 <= encoder_value < LOW_COMPENSATION_LIMIT:
            target_rpm = config.user_spool_rpm * (
                        1 + ((LOW_COMPENSATION_LIMIT - encoder_value) / LOW_COMPENSATION_LIMIT) * RPM_UP_K)
        elif encoder_value > HIGH_COMPENSATION_LIMIT:
            target_rpm = config.user_spool_rpm * (
                        1 - ((encoder_value - HIGH_COMPENSATION_LIMIT) / HIGH_COMPENSATION_LIMIT) * RPM_UP_K)

        if self._prev_rpm != target_rpm:
            self._prev_rpm = target_rpm
        self.steppers.set_sync_rpm(max(0, int(target_rpm)))

    def get_meters(self):
        return self.finished_filament_meters

    def check_finished_meters(self):
        try:
            self.finished_filament_meters = self.encoders.get_meters()
        except:
            pass

        left = config.filament_meters - self.finished_filament_meters

        if left <= 0:
            logger.info("Target reached! Auto-parking...")
            threading.Thread(target=self.bip, args=(1000, 3), daemon=True).start()
            self.park_carriege()
        elif 10 < left < self._meters_left_to_bip:
            threading.Thread(target=self.bip, args=(250, 3), daemon=True).start()
            self._meters_left_to_bip -= 5

    def reset_winding_state(self):
        logger.info("Resetting meters and state")
        try:
            self.encoders.clear_encoder_values()
        except:
            pass
        self._meters_left_to_bip = 100
        self.finished_filament_meters = 0.0
        self._prev_rpm = 0

    def set_filament_thickness(self, thickness):
        config.filament_thickness = thickness
        if self.is_filament_winding:
            self.steppers.set_diameter(thickness)
        logger.info(f"Filament thickness set to: {thickness} mm")

    def set_spool_width(self, width):
        config.spool_width = width
        if self.is_filament_winding:
            self.steppers.set_width(width)
        logger.info(f"Spool width set to: {width} mm")

    def set_spool_rpm(self, rpm):
        config.user_spool_rpm = rpm
        if self.is_filament_winding:
            self.motors_rpm_compensation()
        logger.info(f"Target RPM set to: {rpm}")

    def _loop_safety_monitor(self):
        while self.is_filament_winding:
            if detector.is_change_left_en():
                self.stop_filament_winding()
                threading.Thread(target=self.bip, args=(80, 15), daemon=True).start()
                break
            time.sleep(0.05)

    def _loop_compensation(self):
        while self.is_filament_winding:
            try:
                self.motors_rpm_compensation()
            except Exception as e:
                logger.error(f'Comp error: {e}')
            time.sleep(0.1)

    def _loop_meters(self):
        while self.is_filament_winding:
            try:
                self.check_finished_meters()
            except Exception as e:
                logger.error(f'Meters error: {e}')
            time.sleep(0.5)

    def bip(self, delay=BIP_DELAY, count=BIP_COUNT):
        if self.is_bip: return
        self.is_bip = True
        detector.bip(count, delay)
        self.is_bip = False