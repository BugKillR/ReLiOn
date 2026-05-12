from fastapi import APIRouter
import logging
from app.database.mongodb import db
from app.models.battery import BatteryInput

router = APIRouter()

@router.post("/analyze")
async def analyze_battery(data: BatteryInput):

    soh = max(100 - (data.cycles * 0.02), 50)

    profitability = data.capacity * 0.5

    if soh > 80:
        risk = "Low"
    elif soh > 65:
        risk = "Medium"
    else:
        risk = "High"

    result = {
        "batteryType": data.batteryType,
        "capacity": data.capacity,
        "cycles": data.cycles,
        "soh": round(soh, 2),
        "profitability": round(profitability, 2),
        "risk": risk
    }

    try:
        await db.analysis.insert_one(result)
    except Exception as e:
        logging.exception("Failed to save analysis to DB: %s", e)

    return {
        "success": True,
        "data": result
    }