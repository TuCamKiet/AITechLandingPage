from fastapi import APIRouter

from app.schemas.landing_schema.pricing_schema import Pricing
from app.services.landing_service.pricing_service import PricingService

router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"]
)


@router.get("/", response_model=list[Pricing])
async def get_pricing():
    return PricingService.get_all_pricing()