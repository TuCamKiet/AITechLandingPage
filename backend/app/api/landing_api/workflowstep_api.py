from fastapi import APIRouter

from app.schemas.landing_schema.workflowstep_schema import WorkflowStep
from app.services.landing_service.workflowstep_service import WorkflowStepService

router = APIRouter(
    prefix="/workflowsteps",
    tags=["WorkflowSteps"]
)


@router.get("/", response_model=list[WorkflowStep])
async def get_workflowsteps():
    return WorkflowStepService.get_all_workflowsteps()