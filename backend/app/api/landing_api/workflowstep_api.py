from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.db_dependency import get_db

from app.schemas.landing_schema.workflowstep_schema import (
    WorkflowStepCreate,
    WorkflowStepUpdate,
    WorkflowStepResponse
)

from app.services.landing_service.workflowstep_service import (
    get_all_workflow_steps,
    get_workflow_step_by_id,
    create_workflow_step,
    update_workflow_step,
    delete_workflow_step
)

router = APIRouter(
    prefix="/workflow-steps",
    tags=["Workflow Steps"]
)

# GET ALL
@router.get(
    "",
    response_model=list[WorkflowStepResponse]
)
def get_workflow_steps(
    db: Session = Depends(get_db)
):
    return get_all_workflow_steps(db)

# GET BY ID
@router.get(
    "/{workflow_step_id}",
    response_model=WorkflowStepResponse
)
def get_workflow_step(
    workflow_step_id: int,
    db: Session = Depends(get_db)
):
    workflow_step = get_workflow_step_by_id(
        db,
        workflow_step_id
    )

    if not workflow_step:
        raise HTTPException(
            status_code=404,
            detail="Workflow step not found"
        )

    return workflow_step

# CREATE
@router.post(
    "",
    response_model=WorkflowStepResponse,
    status_code=201
)
def create_new_workflow_step(
    workflow_step_data: WorkflowStepCreate,
    db: Session = Depends(get_db)
):
    return create_workflow_step(
        db,
        workflow_step_data
    )

# UPDATE
@router.put(
    "/{workflow_step_id}",
    response_model=WorkflowStepResponse
)
def update_existing_workflow_step(
    workflow_step_id: int,
    workflow_step_data: WorkflowStepUpdate,
    db: Session = Depends(get_db)
):
    workflow_step = update_workflow_step(
        db,
        workflow_step_id,
        workflow_step_data
    )

    if not workflow_step:
        raise HTTPException(
            status_code=404,
            detail="Workflow step not found"
        )

    return workflow_step

# DELETE
@router.delete(
    "/{workflow_step_id}"
)
def remove_workflow_step(
    workflow_step_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_workflow_step(
        db,
        workflow_step_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Workflow step not found"
        )

    return {
        "message": "Workflow step deleted successfully"
    }