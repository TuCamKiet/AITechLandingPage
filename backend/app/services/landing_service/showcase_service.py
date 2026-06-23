from sqlalchemy.orm import Session

from app.models.landing_model.showcase_model import Showcase
from app.schemas.landing_schema.showcase_schema import (
    ShowcaseCreate,
    ShowcaseUpdate
)


def get_all_showcases(db: Session):
    return db.query(Showcase).all()


def get_showcase_by_id(
    db: Session,
    showcase_id: int
):
    return (
        db.query(Showcase)
        .filter(Showcase.id == showcase_id)
        .first()
    )


def create_showcase(
    db: Session,
    showcase_data: ShowcaseCreate
):
    showcase = Showcase(
        icon=showcase_data.icon,
        title=showcase_data.title,
        description=showcase_data.description,
        metric=showcase_data.metric
    )

    db.add(showcase)
    db.commit()
    db.refresh(showcase)

    return showcase


def update_showcase(
    db: Session,
    showcase_id: int,
    showcase_data: ShowcaseUpdate
):
    showcase = get_showcase_by_id(
        db,
        showcase_id
    )

    if not showcase:
        return None

    showcase.icon = showcase_data.icon
    showcase.title = showcase_data.title
    showcase.description = showcase_data.description
    showcase.metric = showcase_data.metric

    db.commit()
    db.refresh(showcase)

    return showcase


def delete_showcase(
    db: Session,
    showcase_id: int
):
    showcase = get_showcase_by_id(
        db,
        showcase_id
    )

    if not showcase:
        return False

    db.delete(showcase)
    db.commit()

    return True