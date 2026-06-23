from pydantic import BaseModel


class StatCreate(BaseModel):
    label: str
    value: str


class StatUpdate(BaseModel):
    label: str
    value: str


class StatResponse(BaseModel):
    id: int
    label: str
    value: str

    model_config = {
        "from_attributes": True
    }