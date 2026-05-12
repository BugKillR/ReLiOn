from pydantic import BaseModel, Field
from typing import Literal

class BatteryInput(BaseModel):
    batteryType: Literal["LFP", "NMC", "NCA"]
    capacity: float = Field(..., ge=0, le=100)
    cycles: int = Field(..., ge=0)