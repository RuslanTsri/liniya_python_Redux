from fastapi import APIRouter
from core.settings import config

router = APIRouter()
winding_ref = None  # Сюди ми передамо мізки з main.py

def setup_routes(app, winding_process):
    global winding_ref
    winding_ref = winding_process
    app.include_router(router)

@router.get("/api/status")
async def get_status():
    """Фронтенд буде викликати це кожні 500мс, щоб оновити цифри на екрані"""
    return {
        "meters": round(winding_ref.get_meters(), 2),
        "is_winding": winding_ref.is_filament_winding,
        "is_parking": winding_ref.is_parking,
        "current_rpm": winding_ref._prev_rpm
    }

@router.get("/api/config")
async def get_app_config():
    """Віддає поточні налаштування з вашого config.json"""
    return {
        "rpm": config.user_spool_rpm,
        "thickness": config.filament_thickness,
        "width": config.spool_width
    }

@router.post("/api/start")
async def start_winding():
    winding_ref.start_filament_winding()
    return {"status": "started"}

@router.post("/api/stop")
async def stop_winding():
    winding_ref.stop_filament_winding()
    return {"status": "stopped"}