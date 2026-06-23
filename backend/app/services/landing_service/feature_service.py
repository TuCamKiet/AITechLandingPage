from sqlalchemy.orm import Session

from app.models.landing_model.feature_model import Feature
from app.schemas.landing_schema.feature_schema import (
    FeatureCreate,
    FeatureUpdate
)


def get_all_features(db: Session):
    return db.query(Feature).all()


def get_feature_by_id(
    db: Session,
    feature_id: int
):
    return (
        db.query(Feature)
        .filter(Feature.id == feature_id)
        .first()
    )


def create_feature(
    db: Session,
    feature_data: FeatureCreate
):
    feature = Feature(
        icon=feature_data.icon,
        title=feature_data.title,
        description=feature_data.description
    )

    db.add(feature)
    db.commit()
    db.refresh(feature)

    return feature


def update_feature(
    db: Session,
    feature_id: int,
    feature_data: FeatureUpdate
):
    feature = get_feature_by_id(
        db,
        feature_id
    )

    if not feature:
        return None

    feature.icon = feature_data.icon
    feature.title = feature_data.title
    feature.description = feature_data.description

    db.commit()
    db.refresh(feature)

    return feature


def delete_feature(
    db: Session,
    feature_id: int
):
    feature = get_feature_by_id(
        db,
        feature_id
    )

    if not feature:
        return False

    db.delete(feature)
    db.commit()

    return True