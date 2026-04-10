import json
import os
from utils.logger import logger

class AppConfig:
    CONFIG_PATH = 'config.json'

    def __init__(self):
        self._data = {
            "user_spool_rpm": 120,
            "filament_meters": 800.0,
            "filament_thickness": 1.75,
            "spool_width": 80.0,
            "parking_margin": 0.0
        }
        self._load()

    def _load(self):
        if os.path.exists(self.CONFIG_PATH):
            try:
                with open(self.CONFIG_PATH, 'r', encoding='utf-8') as f:
                    self._data.update(json.load(f))
            except Exception as e:
                logger.error(f"Помилка читання config.json: {e}")
        else:
            self._save()

    def _save(self):
        try:
            with open(self.CONFIG_PATH, 'w', encoding='utf-8') as f:
                json.dump(self._data, f, indent=4)
        except Exception as e:
            logger.error(f"Помилка запису config.json: {e}")

    @property
    def user_spool_rpm(self): return self._data.get("user_spool_rpm", 120)

    @user_spool_rpm.setter
    def user_spool_rpm(self, value):
        self._data["user_spool_rpm"] = round(float(value), 2)
        self._save()

    @property
    def filament_meters(self): return self._data.get("filament_meters", 800.0)

    @filament_meters.setter
    def filament_meters(self, value):
        self._data["filament_meters"] = round(float(value), 2)
        self._save()

    @property
    def filament_thickness(self): return self._data.get("filament_thickness", 1.75)

    @filament_thickness.setter
    def filament_thickness(self, value):
        self._data["filament_thickness"] = round(float(value), 3)
        self._save()

    @property
    def spool_width(self): return self._data.get("spool_width", 80.0)

    @spool_width.setter
    def spool_width(self, value):
        self._data["spool_width"] = round(float(value), 2)
        self._save()

    @property
    def parking_margin(self): return self._data.get("parking_margin", 0.0)

    @parking_margin.setter
    def parking_margin(self, value):
        self._data["parking_margin"] = round(float(value), 2)
        self._save()

config = AppConfig()