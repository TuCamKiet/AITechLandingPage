from pydantic import BaseModel
class Showcase(BaseModel):
    icon: str
    title: str
    description: str
    metric: str