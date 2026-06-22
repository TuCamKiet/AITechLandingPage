from fastapi import APIRouter
from app.services.landing_service.landing_service import LandingService

router = APIRouter(
    prefix="/landing",
    tags=["Landing"]
)


@router.get("")
def get_landing_page():
    return LandingService.get_landing_data()