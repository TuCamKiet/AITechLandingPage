from app.data.landing_data import workflowSteps
from app.schemas.landing_schema.workflowstep_schema import WorkflowStep


class WorkflowStepService:
    @staticmethod
    def get_all_workflowsteps() -> list[WorkflowStep]:
        return [WorkflowStep(**item) for item in workflowSteps]