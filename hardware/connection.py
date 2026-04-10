import time

from utils import logger
import serial


class ArduinoConnectionError(Exception):
    pass


def find_arduino(success_answer, success_response, baudrate=9600):
    ports = [f'/dev/ttyACM{i}' for i in range(10)] + [f'/dev/ttyUSB{i}' for i in range(10)]
    for port in ports:
        try:
            ser = serial.Serial(port, baudrate, timeout=1)
            start_time = time.time()
            for _ in range(10):
                # print(ser.readline().decode('utf-8'))
                if ser.in_waiting > 0:
                    response = ser.readline().decode('utf-8').strip()
                    if response == success_response:
                        logger.info(f"The device {success_response} found on port {port}")
                        ser.write(f'{success_answer}\r\n'.encode('utf-8'))
                        # while True:
                        #    print(ser.readline().decode('utf-8'))
                        return ser
                time.sleep(0.2)

        except (serial.SerialException, OSError):
            continue

    raise ArduinoConnectionError("Could not find arduino on USB ports")
