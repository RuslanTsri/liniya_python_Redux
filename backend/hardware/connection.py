import time
import serial
import sys
from utils.logger import logger


class ArduinoConnectionError(Exception):
    pass


# --- ЗАГЛУШКА ДЛЯ ТЕСТУВАННЯ БЕЗ АРДУІНО ---
class MockSerial:
    def __init__(self, name):
        self.name = name
        self.in_waiting = 0
        logger.warning(f"Використовується віртуальна заглушка (MockSerial) для: {name}")

    def write(self, data):
        pass

    def read(self, size=1):
        time.sleep(0.1)  # Щоб не перевантажити процесор нескінченними циклами
        return b''

    def readline(self):
        time.sleep(0.1)
        return b''

    def reset_input_buffer(self):
        pass

    def flush(self):
        pass

    def close(self):
        pass


def find_arduino(success_answer, success_response, baudrate=9600):
    """
    Шукає Ардуіно по всіх доступних портах. Якщо не знаходить — повертає заглушку.
    """
    # Додаємо підтримку Windows (COM порти) та Linux (Raspberry Pi)
    if sys.platform.startswith('win'):
        ports = [f'COM{i}' for i in range(1, 20)]
    else:
        ports = [f'/dev/ttyACM{i}' for i in range(10)] + [f'/dev/ttyUSB{i}' for i in range(10)]

    for port in ports:
        try:
            ser = serial.Serial(port, baudrate, timeout=1)
            for _ in range(10):
                if ser.in_waiting > 0:
                    # errors='ignore' допомагає, якщо прилетить битий байт
                    response = ser.readline().decode('utf-8', errors='ignore').strip()
                    if response == success_response:
                        logger.info(f"Пристрій {success_response} знайдено на порту {port}")
                        ser.write(f'{success_answer}\r\n'.encode('utf-8'))
                        return ser
                time.sleep(0.2)
            ser.close()  # Закриваємо порт, якщо це не та Ардуінка
        except (serial.SerialException, OSError):
            continue

    logger.error(f"Не вдалося знайти фізичну плату '{success_response}'. Вмикаємо емуляцію (Mock).")

    # Замість raise ArduinoConnectionError(...) повертаємо заглушку
    return MockSerial(success_response)