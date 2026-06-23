from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.db_dependency import get_db

from app.schemas.landing_schema.feature_schema import (
    FeatureCreate,
    FeatureUpdate,
    FeatureResponse
)

from app.services.landing_service.feature_service import (
    get_all_features,
    get_feature_by_id,
    create_feature,
    update_feature,
    delete_feature
)

router = APIRouter(
    prefix="/features",
    tags=["Features"]
)

# GET ALL
@router.get(
    "",
    response_model=list[FeatureResponse]
)
def get_features(
    db: Session = Depends(get_db)
):
    return get_all_features(db)

# GET BY ID
@router.get(
    "/{feature_id}",
    response_model=FeatureResponse
)
def get_feature(
    feature_id: int,
    db: Session = Depends(get_db)
):
    feature = get_feature_by_id(
        db,
        feature_id
    )

    if not feature:
        raise HTTPException(
            status_code=404,
            detail="Feature not found"
        )

    return feature

# CREATE
@router.post(
    "",
    response_model=FeatureResponse,
    status_code=201
)
def create_new_feature(
    feature_data: FeatureCreate,
    db: Session = Depends(get_db)
):
    return create_feature(
        db,
        feature_data
    )

# UPDATE
@router.put(
    "/{feature_id}",
    response_model=FeatureResponse
)
def update_existing_feature(
    feature_id: int,
    feature_data: FeatureUpdate,
    db: Session = Depends(get_db)
):
    feature = update_feature(
        db,
        feature_id,
        feature_data
    )

    if not feature:
        raise HTTPException(
            status_code=404,
            detail="Feature not found"
        )

    return feature

# DELETE
@router.delete(
    "/{feature_id}"
)
def remove_feature(
    feature_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_feature(
        db,
        feature_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Feature not found"
        )

    return {
        "message": "Feature deleted successfully"
    }