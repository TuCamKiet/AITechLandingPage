from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.db_dependency import get_db

from app.schemas.landing_schema.integration_schema import (
    IntegrationCreate,
    IntegrationUpdate,
    IntegrationResponse
)

from app.services.landing_service.integration_service import (
    get_all_integrations,
    get_integration_by_id,
    create_integration,
    update_integration,
    delete_integration
)

router = APIRouter(
    prefix="/integrations",
    tags=["Integrations"]
)

# GET ALL
@router.get(
    "",
    response_model=list[IntegrationResponse]
)
def get_integrations(
    db: Session = Depends(get_db)
):
    return get_all_integrations(db)

# GET BY ID
@router.get(
    "/{integration_id}",
    response_model=IntegrationResponse
)
def get_integration(
    integration_id: int,
    db: Session = Depends(get_db)
):
    integration = get_integration_by_id(
        db,
        integration_id
    )

    if not integration:
        raise HTTPException(
            status_code=404,
            detail="Integration not found"
        )

    return integration

# CREATE
@router.post(
    "",
    response_model=IntegrationResponse,
    status_code=201
)
def create_new_integration(
    integration_data: IntegrationCreate,
    db: Session = Depends(get_db)
):
    return create_integration(
        db,
        integration_data
    )

# UPDATE
@router.put(
    "/{integration_id}",
    response_model=IntegrationResponse
)
def update_existing_integration(
    integration_id: int,
    integration_data: IntegrationUpdate,
    db: Session = Depends(get_db)
):
    integration = update_integration(
        db,
        integration_id,
        integration_data
    )

    if not integration:
        raise HTTPException(
            status_code=404,
            detail="Integration not found"
        )

    return integration

# DELETE
@router.delete(
    "/{integration_id}"
)
def remove_integration(
    integration_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_integration(
        db,
        integration_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Integration not found"
        )

    return {
        "message": "Integration deleted successfully"
    }