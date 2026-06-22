from fastapi import APIRouter

from app.schemas.landing_schema.service_schema import Service
from app.services.landing_service.service_service import ServiceService

router = APIRouter(
    prefix="/services",
    tags=["Services"]
)


@router.get("/", response_model=list[Service])
async def get_services():
    return ServiceService.get_all_services()