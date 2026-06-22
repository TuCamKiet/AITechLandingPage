from fastapi import APIRouter

from app.schemas.landing_schema.stat_schema import Stat
from app.services.landing_service.stat_service import StatService

router = APIRouter(
    prefix="/stats",
    tags=["Stats"]
)


@router.get("/", response_model=list[Stat])
async def get_stats():
    return StatService.get_all_stats()