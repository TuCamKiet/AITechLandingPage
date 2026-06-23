from pydantic import BaseModel


class WorkflowStepBase(BaseModel):
    step: str
    title: str
    detail: str


class WorkflowStepCreate(WorkflowStepBase):
    pass


class WorkflowStepUpdate(WorkflowStepBase):
    pass


class WorkflowStepResponse(WorkflowStepBase):
    id: int

    model_config = {
        "from_attributes": True
    }