from pydantic import BaseModel

class AirQualitySchema(BaseModel):
    status: str
    data: dict
    