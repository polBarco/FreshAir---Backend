from fastapi import APIRouter, HTTPException
from services.Air import AirQualityService
from schemas.Air import AirQualitySchema
from core.config import AQICN_API_TOKEN

router = APIRouter()

@router.get("/feed/{city}", tags=["Air"], response_model=AirQualitySchema)
async def get_air_paramns(city: str):
    try:
        air_paramns = await AirQualityService.get_air_quality(city, AQICN_API_TOKEN)
        return air_paramns
    except Exception:
        raise HTTPException(status_code=404, detail='City not found')