from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.db_dependency import get_db

from app.schemas.landing_schema.preview_schema import (
    PreviewCreate,
    PreviewUpdate,
    PreviewResponse
)

from app.services.landing_service.preview_service import (
    get_all_previews,
    get_preview_by_id,
    create_preview,
    update_preview,
    delete_preview
)

router = APIRouter(
    prefix="/previews",
    tags=["Previews"]
)

# GET ALL
@router.get(
    "",
    response_model=list[PreviewResponse]
)
def get_previews(
    db: Session = Depends(get_db)
):
    return get_all_previews(db)

# GET BY ID
@router.get(
    "/{preview_id}",
    response_model=PreviewResponse
)
def get_preview(
    preview_id: int,
    db: Session = Depends(get_db)
):
    preview = get_preview_by_id(
        db,
        preview_id
    )

    if not preview:
        raise HTTPException(
            status_code=404,
            detail="Preview not found"
        )

    return preview

# CREATE
@router.post(
    "",
    response_model=PreviewResponse,
    status_code=201
)
def create_new_preview(
    preview_data: PreviewCreate,
    db: Session = Depends(get_db)
):
    return create_preview(
        db,
        preview_data
    )

# UPDATE
@router.put(
    "/{preview_id}",
    response_model=PreviewResponse
)
def update_existing_preview(
    preview_id: int,
    preview_data: PreviewUpdate,
    db: Session = Depends(get_db)
):
    preview = update_preview(
        db,
        preview_id,
        preview_data
    )

    if not preview:
        raise HTTPException(
            status_code=404,
            detail="Preview not found"
        )

    return preview

# DELETE
@router.delete(
    "/{preview_id}"
)
def remove_preview(
    preview_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_preview(
        db,
        preview_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Preview not found"
        )

    return {
        "message": "Preview deleted successfully"
    }