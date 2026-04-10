import threading
import re
import time
from hardware.connection import find_arduino

class EncoderArduino:
    def __init__(self, baudrate=500000):
        self.arduino = find_arduino('ok', 'encoders', baudrate)
        self.prev_meters = 0.0
        self.prev_comp_value = 0
        self._lock = threading.Lock()
        self._running = True

        self._reader_thread = threading.Thread(target=self._read_loop, daemon=True)
        self._reader_thread.start()

    def get_meters(self):
        with self._lock:
            return self.prev_meters

    def get_compensation_encoder_value(self):
        with self._lock:
            return self.prev_comp_value

    def clear_encoder_values(self):
        for _ in range(3):
            self.arduino.write(b'clear\n')
            time.sleep(0.01)

    def _parse_line(self, line):
        match = re.match(r"m:(-?[\d\.]+)\|e:(-?\d+)", line)
        if match:
            try:
                meters = float(match.group(1))
                encoder_val = int(match.group(2))
                with self._lock:
                    self.prev_meters = meters
                    self.prev_comp_value = encoder_val
            except ValueError:
                pass

    def _read_loop(self):
        buffer = ""
        while self._running:
            try:
                byte = self.arduino.read(1)
                if byte:
                    char = byte.decode('utf-8', errors='ignore')
                    if char == '\n':
                        self._parse_line(buffer.strip())
                        buffer = ""
                    else:
                        buffer += char
            except Exception:
                continue