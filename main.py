import sys
import traceback
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import qInstallMessageHandler
from utils.logger import logger

# Імпортуємо переписані шари
from hardware.drivers import DriversArduino
from hardware.encoders import EncoderArduino
from hardware.steppers import Steppers
from core.winding import WindingProcess
from windows.main_window import MainWindow

class LogStreamProxy:
    def __init__(self, log_func):
        self.log_func = log_func
        self.buffer = ""

    def write(self, message):
        if message.strip():
            self.log_func(message.strip())

    def flush(self):
        pass

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    err_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    logger.error(f"Uncaught exception:\n{err_msg}")

def qt_message_handler(mode, context, message):
    msg = f"Qt {context.category}: {message}"
    if mode == 0: logger.debug(msg)
    elif mode == 1: logger.warning(msg)
    elif mode == 2: logger.error(msg)
    else: logger.info(msg)

sys.stdout = LogStreamProxy(logger.info)
sys.stderr = LogStreamProxy(logger.error)
sys.excepthook = handle_exception
qInstallMessageHandler(qt_message_handler)

logger.info('init app')
app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(True)

# 1. СТВОРЮЄМО ЗАЛІЗО
drivers = DriversArduino()
encoders = EncoderArduino(baudrate=500000)
steppers = Steppers(drivers=drivers)

# 2. СТВОРЮЄМО ЛОГІКУ
winding_process = WindingProcess(steppers=steppers, encoders=encoders)

# 3. ПЕРЕДАЄМО ЛОГІКУ У ВІКНО
widget = MainWindow(winding_process=winding_process)

def main():
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

logger.info('finish init main.py')