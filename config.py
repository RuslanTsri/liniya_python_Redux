import os
from dotenv import load_dotenv
from utils.logger import logger

# --- ЗАХИСТ ВІД ЗАПУСКУ НА ПК (Заглушка для GPIO) ---
try:
    import RPi.GPIO as GPIO
except ImportError:
    logger.warning("RPi.GPIO не знайдено! Використовуємо заглушку для запуску на ПК.")
    class MockGPIO:
        HIGH = 1
        LOW = 0
        BCM = 'BCM'
        IN = 'IN'
        OUT = 'OUT'
        PUD_UP = 'PUD_UP'
        PUD_DOWN = 'PUD_DOWN'
        FALLING = 'FALLING'
        RISING = 'RISING'
        BOTH = 'BOTH'
        def setmode(self, *args): pass
        def setup(self, *args, **kwargs): pass
        def output(self, *args): pass
        def input(self, *args): return self.LOW
        def add_event_detect(self, *args, **kwargs): pass
        def cleanup(self): pass
    GPIO = MockGPIO()
# --------------------------------------------------

load_dotenv()
IS_FULL_SCREEN = True
IS_PHYSICAL_BUTTON = True
IS_FAKE_CHANGE_DETECTORS = False
GOOGLE_API_URL = "https://www.googleapis.com"
IS_CHANGE_RIGHT_DISABLED = True
CODENAME = os.getenv('codename')
logger.info(f'CODENAME: {CODENAME}')

MINUS_PARKING_HOMING_VALUE = {
    'leopold': 1,
    'yaro': 0,
}.get(CODENAME, 0)  # value that already "done" in mm

CARRIEGE_STEPS_K = {
    'deadline': 1.5,
    'winding-03': 1.25,
    'yaro': 1.0,
}.get(CODENAME, 1.0)

DRIVER_STEPS_DIVIDE = 1
HOMING_CARRIEGE_SPEED = 1500
IS_CARRIEGE_DIRECTION_REVERSED = True

BIP_DELAY = 1000  # pause for bip
BIP_COUNT = 3  # count of bip
BIP_PIN = 23

LOW_COMPENSATION_LIMIT = {
    'winding-03': 150,
    'leopold': 300,
    'deadline':150,
    'yaro': 150,
}.get(CODENAME, 150)

HIGH_COMPENSATION_LIMIT = {
    'winding-03': 300,
    'leopold': 400,
    'deadline': 300,
    'yaro': 300
}.get(CODENAME, 300)

RPM_UP_K = 2

CHANGE_RIGHT_PIN = {
    'leopold': 29,
}.get(CODENAME, 29)
CHANGE_LEFT_PIN = 19

STOP_BTN_PIN =  33
RUN_BTN_PIN = 7

CHANGE_RIGHT_EN_STATE = GPIO.HIGH
CHANGE_LEFT_EN_STATE = GPIO.LOW
STOP_BTN_EN_STATE = GPIO.HIGH
RUN_BTN_EN_STATE = GPIO.LOW

CARRIEGE_STEPS_BY_REVOL = {
    'leopold': 1000,
    'deadline': 400,
    'winding-03': 400,
}.get(CODENAME, 400)

CARRIEGE_MM_PER_REVOL = {
    'leopold': 10,
    'deadline': 5,
    'winding-03': 10,
}.get(CODENAME, 5)

YARO_COMPENSATION = 'yaro_compensation'
FILAMENT_COMPENSATION_TYPE = None
COMPENSATOR_PINS = {
    YARO_COMPENSATION: {
        'up_signal': 5,
        'down_signal': 24,
        'stop_signal': 22,
        'stop_change': 16,
    }
}

SELECTED_BUTTON_STYLE_UI = "background-color : #3858A9;font: 22pt Furore; color: #fff; border: none; border-radius: 7px;"
UNSELECTED_BUTTON_STYLE_UI = "background-color : #38A962;font: 22pt Furore; color: #fff; border: none; border-radius: 7px;"