from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.db_dependency import get_db

from app.schemas.landing_schema.teammenber_schema import (
    TeamMemberCreate,
    TeamMemberUpdate,
    TeamMemberResponse
)

from app.services.landing_service.teammember_service import (
    get_all_team_members,
    get_team_member_by_id,
    create_team_member,
    update_team_member,
    delete_team_member
)

router = APIRouter(
    prefix="/team-members",
    tags=["Team Members"]
)

# GET ALL
@router.get(
    "",
    response_model=list[TeamMemberResponse]
)
def get_team_members(
    db: Session = Depends(get_db)
):
    return get_all_team_members(db)

# GET BY ID
@router.get(
    "/{member_id}",
    response_model=TeamMemberResponse
)
def get_team_member(
    member_id: int,
    db: Session = Depends(get_db)
):
    member = get_team_member_by_id(
        db,
        member_id
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Team member not found"
        )

    return member

# CREATE
@router.post(
    "",
    response_model=TeamMemberResponse,
    status_code=201
)
def create_new_team_member(
    member_data: TeamMemberCreate,
    db: Session = Depends(get_db)
):
    return create_team_member(
        db,
        member_data
    )

# UPDATE
@router.put(
    "/{member_id}",
    response_model=TeamMemberResponse
)
def update_existing_team_member(
    member_id: int,
    member_data: TeamMemberUpdate,
    db: Session = Depends(get_db)
):
    member = update_team_member(
        db,
        member_id,
        member_data
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Team member not found"
        )

    return member

# DELETE
@router.delete(
    "/{member_id}"
)
def remove_team_member(
    member_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_team_member(
        db,
        member_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Team member not found"
        )

    return {
        "message": "Team member deleted successfully"
    }