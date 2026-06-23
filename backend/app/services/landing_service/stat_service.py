from sqlalchemy.orm import Session

from app.models.landing_model.stat_model import Stat
from app.schemas.landing_schema.stat_schema import (
    StatCreate,
    StatUpdate,
)


def get_all_stats(db: Session):
    return db.query(Stat).all()


def get_stat_by_id(
    db: Session,
    stat_id: int,
):
    return (
        db.query(Stat)
        .filter(Stat.id == stat_id)
        .first()
    )


def create_stat(
    db: Session,
    stat_data: StatCreate,
):
    stat = Stat(
        label=stat_data.label,
        value=stat_data.value,
    )

    db.add(stat)
    db.commit()
    db.refresh(stat)

    return stat


def update_stat(
    db: Session,
    stat_id: int,
    stat_data: StatUpdate,
):
    stat = get_stat_by_id(
        db,
        stat_id,
    )

    if not stat:
        return None

    stat.label = stat_data.label
    stat.value = stat_data.value

    db.commit()
    db.refresh(stat)

    return stat


def delete_stat(
    db: Session,
    stat_id: int,
):
    stat = get_stat_by_id(
        db,
        stat_id,
    )

    if not stat:
        return False

    db.delete(stat)
    db.commit()

    return True