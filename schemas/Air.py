from pydantic import BaseModel
from typing import Dict, Any

class AirQualitySchema(BaseModel):
    status: str
    data: Dict[str, Any]
