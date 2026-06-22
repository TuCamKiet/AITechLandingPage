from pydantic import BaseModel
class WorkflowStep(BaseModel):
    step: str
    title: str
    detail: str