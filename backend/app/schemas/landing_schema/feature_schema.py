from pydantic import BaseModel
class Feature(BaseModel):
    icon: str
    title: str
    description: str