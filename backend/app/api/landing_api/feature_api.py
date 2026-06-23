from fastapi import APIRouter

from app.schemas.landing_schema.feature_schema import Feature
from app.services.landing_service.feature_service import FeatureService

router = APIRouter(
    prefix="/features",
    tags=["Features"]
)


@router.get("/", response_model=list[Feature])
async def get_features():
    return FeatureService.get_all_features()