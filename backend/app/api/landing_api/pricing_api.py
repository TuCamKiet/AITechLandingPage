from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.db_dependency import get_db

from app.schemas.landing_schema.pricing_schema import (
    PricingCreate,
    PricingUpdate,
    PricingResponse
)

from app.services.landing_service.pricing_service import (
    get_all_pricing,
    get_pricing_by_id,
    create_pricing,
    update_pricing,
    delete_pricing
)

router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"]
)

# GET ALL
@router.get(
    "",
    response_model=list[PricingResponse]
)
def get_pricing(
    db: Session = Depends(get_db)
):
    return get_all_pricing(db)

# GET BY ID
@router.get(
    "/{pricing_id}",
    response_model=PricingResponse
)
def get_pricing_item(
    pricing_id: int,
    db: Session = Depends(get_db)
):
    pricing = get_pricing_by_id(
        db,
        pricing_id
    )

    if not pricing:
        raise HTTPException(
            status_code=404,
            detail="Pricing not found"
        )

    return pricing

# CREATE
@router.post(
    "",
    response_model=PricingResponse,
    status_code=201
)
def create_pricing_item(
    pricing_data: PricingCreate,
    db: Session = Depends(get_db)
):
    return create_pricing(
        db,
        pricing_data
    )

# UPDATE
@router.put(
    "/{pricing_id}",
    response_model=PricingResponse
)
def update_pricing_item(
    pricing_id: int,
    pricing_data: PricingUpdate,
    db: Session = Depends(get_db)
):
    pricing = update_pricing(
        db,
        pricing_id,
        pricing_data
    )

    if not pricing:
        raise HTTPException(
            status_code=404,
            detail="Pricing not found"
        )

    return pricing

# DELETE
@router.delete(
    "/{pricing_id}"
)
def delete_pricing_item(
    pricing_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_pricing(
        db,
        pricing_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Pricing not found"
        )

    return {
        "message": "Pricing deleted successfully"
    }