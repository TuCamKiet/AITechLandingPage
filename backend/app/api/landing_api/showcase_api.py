from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db_dependency import get_db

from app.schemas.landing_schema.showcase_schema import (
    ShowcaseCreate,
    ShowcaseUpdate,
    ShowcaseResponse
)

from app.services.landing_service.showcase_service import (
    get_all_showcases,
    get_showcase_by_id,
    create_showcase,
    update_showcase,
    delete_showcase
)

router = APIRouter(
    prefix="/showcases",
    tags=["Showcases"]
)

# GET ALL
@router.get(
    "",
    response_model=list[ShowcaseResponse]
)
def get_showcases(
    db: Session = Depends(get_db)
):
    return get_all_showcases(db)

# GET BY ID
@router.get(
    "/{showcase_id}",
    response_model=ShowcaseResponse
)
def get_showcase(
    showcase_id: int,
    db: Session = Depends(get_db)
):
    showcase = get_showcase_by_id(
        db,
        showcase_id
    )

    if not showcase:
        raise HTTPException(
            status_code=404,
            detail="Showcase not found"
        )

    return showcase

# CREATE
@router.post(
    "",
    response_model=ShowcaseResponse,
    status_code=201
)
def create_new_showcase(
    showcase_data: ShowcaseCreate,
    db: Session = Depends(get_db)
):
    return create_showcase(
        db,
        showcase_data
    )

# UPDATE
@router.put(
    "/{showcase_id}",
    response_model=ShowcaseResponse
)
def update_existing_showcase(
    showcase_id: int,
    showcase_data: ShowcaseUpdate,
    db: Session = Depends(get_db)
):
    showcase = update_showcase(
        db,
        showcase_id,
        showcase_data
    )

    if not showcase:
        raise HTTPException(
            status_code=404,
            detail="Showcase not found"
        )

    return showcase

# DELETE
@router.delete(
    "/{showcase_id}"
)
def remove_showcase(
    showcase_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_showcase(
        db,
        showcase_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Showcase not found"
        )

    return {
        "message": "Showcase deleted successfully"
    }