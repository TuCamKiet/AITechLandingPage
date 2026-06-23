from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.db_dependency import get_db

from app.schemas.landing_schema.faq_schema import (
    FAQCreate,
    FAQUpdate,
    FAQResponse
)

from app.services.landing_service.faq_service import (
    get_all_faqs,
    get_faq_by_id,
    create_faq,
    update_faq,
    delete_faq
)

router = APIRouter(
    prefix="/faqs",
    tags=["FAQs"]
)

# GET ALL
@router.get(
    "",
    response_model=list[FAQResponse]
)
def get_faqs(
    db: Session = Depends(get_db)
):
    return get_all_faqs(db)

# GET BY ID
@router.get(
    "/{faq_id}",
    response_model=FAQResponse
)
def get_faq(
    faq_id: int,
    db: Session = Depends(get_db)
):
    faq = get_faq_by_id(
        db,
        faq_id
    )

    if not faq:
        raise HTTPException(
            status_code=404,
            detail="FAQ not found"
        )

    return faq

# CREATE
@router.post(
    "",
    response_model=FAQResponse,
    status_code=201
)
def create_new_faq(
    faq_data: FAQCreate,
    db: Session = Depends(get_db)
):
    return create_faq(
        db,
        faq_data
    )

# UPDATE
@router.put(
    "/{faq_id}",
    response_model=FAQResponse
)
def update_existing_faq(
    faq_id: int,
    faq_data: FAQUpdate,
    db: Session = Depends(get_db)
):
    faq = update_faq(
        db,
        faq_id,
        faq_data
    )

    if not faq:
        raise HTTPException(
            status_code=404,
            detail="FAQ not found"
        )

    return faq

# DELETE
@router.delete(
    "/{faq_id}"
)
def remove_faq(
    faq_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_faq(
        db,
        faq_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="FAQ not found"
        )

    return {
        "message": "FAQ deleted successfully"
    }