from fastapi import APIRouter

from app.schemas.landing_schema.faq_schema import FAQ
from app.services.landing_service.faq_service import FaqService

router = APIRouter(
    prefix="/faqs",
    tags=["Faqs"]
)


@router.get("/", response_model=list[FAQ])
async def get_faqs():
    return FaqService.get_all_faqs()