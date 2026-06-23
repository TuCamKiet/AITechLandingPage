from pydantic import BaseModel


class ServiceCreate(BaseModel):
    icon: str
    name: str
    summary: str


class ServiceUpdate(BaseModel):
    icon: str
    name: str
    summary: str


class ServiceResponse(BaseModel):
    id: int
    icon: str
    name: str
    summary: str

    model_config = {
        "from_attributes": True
    }