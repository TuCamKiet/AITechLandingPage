from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.db_dependency import get_db

from app.schemas.landing_schema.service_schema import (
    ServiceCreate,
    ServiceUpdate,
    ServiceResponse
)

from app.services.landing_service.service_service import (
    get_all_services,
    get_service_by_id,
    create_service,
    update_service,
    delete_service
)

router = APIRouter(
    prefix="/services",
    tags=["Services"]
)

#get all
@router.get(
    "",
    response_model=list[ServiceResponse]
)
def get_services(
    db: Session = Depends(get_db)
):
    return get_all_services(db)

#get by id
@router.get(
    "/{service_id}",
    response_model=ServiceResponse
)
def get_service(
    service_id: int,
    db: Session = Depends(get_db)
):
    service = get_service_by_id(
        db,
        service_id
    )

    if not service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    return service

# add new
@router.post(
    "",
    response_model=ServiceResponse,
    status_code=201
)
def create_new_service(
    service_data: ServiceCreate,
    db: Session = Depends(get_db)
):
    return create_service(
        db,
        service_data
    )

# update
@router.put(
    "/{service_id}",
    response_model=ServiceResponse
)
def update_existing_service(
    service_id: int,
    service_data: ServiceUpdate,
    db: Session = Depends(get_db)
):
    service = update_service(
        db,
        service_id,
        service_data
    )

    if not service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    return service

#delete
@router.delete(
    "/{service_id}"
)
def remove_service(
    service_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_service(
        db,
        service_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    return {
        "message": "Service deleted successfully"
    }