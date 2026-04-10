import time
from config import DRIVER_STEPS_DIVIDE, IS_CARRIEGE_DIRECTION_REVERSED, HOMING_CARRIEGE_SPEED, CARRIEGE_STEPS_BY_REVOL
from config import MINUS_PARKING_HOMING_VALUE, CARRIEGE_MM_PER_REVOL
from utils.logger import logger
from hardware.detectors import detector
from core.settings import config


class Steppers:
    # ТЕПЕР ЗАЛІЗО ПЕРЕДАЄТЬСЯ СЮДИ:
    def __init__(self, drivers):
        self.drivers = drivers
        self.last_s1_position = None

    def test_raw_drivers(self):
        print("\n--- Тест DriversArduino (Direct Commands) ---")
        try:
            speed = 600
            print(f"Встановлення швидкості: {speed}")
            self.drivers.set_manual_speed(speed)
            time.sleep(0.5)

            steps = 200
            print(f"Рух вперед: {steps} кроків...")
            self.drivers.move_manual(steps)
            time.sleep(1)

            print(f"Рух назад: {steps} кроків...")
            self.drivers.move_manual(-steps)
            print("Тест завершено успішно.")
        except Exception as e:
            print(f"Помилка: {e}")

    def start_full_sync(self, spool_width_mm, filament_thickness_mm):
        self.drivers.set_width(spool_width_mm)
        self.drivers.set_diameter(filament_thickness_mm)
        self.drivers.set_rpm(config.user_spool_rpm)
        time.sleep(0.1)
        self.drivers.start_winding()

    def update_winding_params(self, spool_width_mm, filament_thickness_mm):
        self.drivers.set_width(spool_width_mm)
        self.drivers.set_diameter(filament_thickness_mm)

    def set_sync_rpm(self, rpm: int):
        self.drivers.set_rpm(rpm)

    def set_diameter(self, diameter: float):
        self.drivers.set_diameter(diameter)

    def set_width(self, width: float):
        self.drivers.set_width(width)

    def stop_sync(self):
        self.drivers.stop_winding()

    def stop_motors(self, _=None):
        logger.info("Stop motors")
        self.drivers.stop_winding()

    def run_carriege_stepper(self, steps):
        steps = steps * -1 if IS_CARRIEGE_DIRECTION_REVERSED else steps
        self.drivers.move_manual(int(steps))

    def homing(self):
        self.drivers.set_manual_speed(HOMING_CARRIEGE_SPEED)
        time.sleep(0.01)

        if detector.is_change_left_en():
            self.run_carriege_stepper(CARRIEGE_STEPS_BY_REVOL)

        while not detector.is_change_left_en():
            self.run_carriege_stepper(-100)

        self.run_carriege_stepper(200)

        while not detector.is_change_left_en():
            self.run_carriege_stepper(-10)

        CHUNK_SIZE = 9000
        steps_ = int(CARRIEGE_STEPS_BY_REVOL * (
                    config.parking_margin - MINUS_PARKING_HOMING_VALUE) / CARRIEGE_MM_PER_REVOL / DRIVER_STEPS_DIVIDE)
        remaining = abs(steps_)
        direction = 1 if steps_ > 0 else -1

        while remaining > 0:
            current_move = min(remaining, CHUNK_SIZE)
            self.run_carriege_stepper(current_move * direction)
            remaining -= current_move

        self.last_s1_position = 'right'