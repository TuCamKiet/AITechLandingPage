from sqlalchemy.orm import Session

from app.models.landing_model.integration_model import Integration


def get_all_integrations(db: Session):
    return db.query(Integration).all()


def get_integration_by_id(
    db: Session,
    integration_id: int
):
    return (
        db.query(Integration)
        .filter(
            Integration.id == integration_id
        )
        .first()
    )


def create_integration(
    db: Session,
    integration_data
):
    integration = Integration(
        name=integration_data.name,
        icon=integration_data.icon
    )

    db.add(integration)

    db.commit()
    db.refresh(integration)

    return integration


def update_integration(
    db: Session,
    integration_id: int,
    integration_data
):
    integration = get_integration_by_id(
        db,
        integration_id
    )

    if not integration:
        return None

    integration.name = integration_data.name
    integration.icon = integration_data.icon

    db.commit()
    db.refresh(integration)

    return integration


def delete_integration(
    db: Session,
    integration_id: int
):
    integration = get_integration_by_id(
        db,
        integration_id
    )

    if not integration:
        return False

    db.delete(integration)

    db.commit()

    return True