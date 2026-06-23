from pydantic import BaseModel


class FeatureCreate(BaseModel):
    icon: str
    title: str
    description: str


class FeatureUpdate(BaseModel):
    icon: str
    title: str
    description: str


class FeatureResponse(BaseModel):
    id: int
    icon: str
    title: str
    description: str

    model_config = {
        "from_attributes": True
    }