from pydantic import BaseModel
class Service(BaseModel):
    icon: str
    name: str
    summary: str