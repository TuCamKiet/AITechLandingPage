from fastapi import APIRouter

from app.schemas.landing_schema.preview_schema import Preview
from app.services.landing_service.preview_service import PreviewService

router = APIRouter(
    prefix="/previews",
    tags=["Previews"]
)


@router.get("/", response_model=list[Preview])
async def get_previews():
    return PreviewService.get_all_previews()