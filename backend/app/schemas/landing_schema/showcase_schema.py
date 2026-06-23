from pydantic import BaseModel


class ShowcaseCreate(BaseModel):
    icon: str
    title: str
    description: str
    metric: str


class ShowcaseUpdate(BaseModel):
    icon: str
    title: str
    description: str
    metric: str


class ShowcaseResponse(BaseModel):
    id: int
    icon: str
    title: str
    description: str
    metric: str

    model_config = {
        "from_attributes": True
    }