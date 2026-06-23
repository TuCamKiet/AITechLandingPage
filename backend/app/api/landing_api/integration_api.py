from fastapi import APIRouter

from app.schemas.landing_schema.integration_schema import Integration
from app.services.landing_service.integration_service import IntegrationService

router = APIRouter(
    prefix="/integrations",
    tags=["Integrations"]
)


@router.get("/", response_model=list[Integration])
async def get_integrations():
    return IntegrationService.get_all_integrations()