from fastapi import APIRouter

from app.schemas.landing_schema.teammenber_schema import TeamMember
from app.services.landing_service.teammember_service import TeamMemberService

router = APIRouter(
    prefix="/teammembers",
    tags=["TeamMembers"]
)


@router.get("/", response_model=list[TeamMember])
async def get_teammembers():
    return TeamMemberService.get_all_teammembers()