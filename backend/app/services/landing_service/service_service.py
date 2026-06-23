from sqlalchemy.orm import Session

from app.models.landing_model.service_model import Service
from app.schemas.landing_schema.service_schema import (
    ServiceCreate,
    ServiceUpdate
)


def get_all_services(db: Session):
    return db.query(Service).all()


def get_service_by_id(
    db: Session,
    service_id: int
):
    return (
        db.query(Service)
        .filter(Service.id == service_id)
        .first()
    )


def create_service(
    db: Session,
    service_data: ServiceCreate
):
    service = Service(
        icon=service_data.icon,
        name=service_data.name,
        summary=service_data.summary
    )

    db.add(service)
    db.commit()
    db.refresh(service)

    return service


def update_service(
    db: Session,
    service_id: int,
    service_data: ServiceUpdate
):
    service = get_service_by_id(
        db,
        service_id
    )

    if not service:
        return None

    service.icon = service_data.icon
    service.name = service_data.name
    service.summary = service_data.summary

    db.commit()
    db.refresh(service)

    return service


def delete_service(
    db: Session,
    service_id: int
):
    service = get_service_by_id(
        db,
        service_id
    )

    if not service:
        return False

    db.delete(service)
    db.commit()

    return True