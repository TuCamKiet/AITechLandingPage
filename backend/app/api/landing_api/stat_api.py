from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.db_dependency import get_db

from app.schemas.landing_schema.stat_schema import (
    StatCreate,
    StatUpdate,
    StatResponse,
)

from app.services.landing_service.stat_service import (
    get_all_stats,
    get_stat_by_id,
    create_stat,
    update_stat,
    delete_stat,
)

router = APIRouter(
    prefix="/stats",
    tags=["Stats"],
)

# get all
@router.get(
    "/",
    response_model=list[StatResponse],
)
def get_stats(
    db: Session = Depends(get_db),
):
    return get_all_stats(db)

# get id
@router.get(
    "/{stat_id}",
    response_model=StatResponse,
)
def get_stat(
    stat_id: int,
    db: Session = Depends(get_db),
):
    stat = get_stat_by_id(
        db,
        stat_id,
    )

    if not stat:
        raise HTTPException(
            status_code=404,
            detail="Stat not found",
        )

    return stat

# add new
@router.post(
    "/",
    response_model=StatResponse,
    status_code=201,
)
def create_new_stat(
    stat_data: StatCreate,
    db: Session = Depends(get_db),
):
    return create_stat(
        db,
        stat_data,
    )

# update
@router.put(
    "/{stat_id}",
    response_model=StatResponse,
)
def update_existing_stat(
    stat_id: int,
    stat_data: StatUpdate,
    db: Session = Depends(get_db),
):
    stat = update_stat(
        db,
        stat_id,
        stat_data,
    )

    if not stat:
        raise HTTPException(
            status_code=404,
            detail="Stat not found",
        )

    return stat

# delete
@router.delete(
    "/{stat_id}",
)
def remove_stat(
    stat_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_stat(
        db,
        stat_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Stat not found",
        )

    return {
        "message": "Stat deleted successfully"
    }