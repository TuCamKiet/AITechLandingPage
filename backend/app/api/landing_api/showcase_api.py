from fastapi import APIRouter

from app.schemas.landing_schema.showcase_schema import Showcase
from app.services.landing_service.showcase_service import ShowcaseService

router = APIRouter(
    prefix="/showcases",
    tags=["Showcases"]
)


@router.get("/", response_model=list[Showcase])
async def get_showcases():
    return ShowcaseService.get_all_showcases()