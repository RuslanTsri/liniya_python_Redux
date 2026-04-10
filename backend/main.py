import sys
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.logger import logger

# Імпортуємо залізо та логіку
from hardware.drivers import DriversArduino
from hardware.encoders import EncoderArduino
from hardware.steppers import Steppers
from core.winding import WindingProcess
from api.routes import setup_routes

# 1. ІНІЦІАЛІЗАЦІЯ FASTAPI
app = FastAPI(title="Filament Winding REDUX API")

# Налаштування CORS, щоб React міг достукатися до API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # У розробці дозволяємо запити з будь-яких адрес
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. СТВОРЮЄМО ЗАЛІЗО
# Ці класи залишаються незмінними, вони просто працюють у фоні
drivers = DriversArduino()
encoders = EncoderArduino(baudrate=500000)
steppers = Steppers(drivers=drivers)

# 3. СТВОРЮЄМО ЛОГІКУ (МІЗКИ)
winding_process = WindingProcess(steppers=steppers, encoders=encoders)

# 4. ПІДКЛЮЧАЄМО МАРШРУТИ API
# Передаємо об'єкт winding_process, щоб API могло ним керувати
setup_routes(app, winding_process)

def main():
    logger.info("Запуск сервера на порту 8000...")
    # host 0.0.0.0 дозволяє підключатися до малинки з будь-якого пристрою в мережі
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()