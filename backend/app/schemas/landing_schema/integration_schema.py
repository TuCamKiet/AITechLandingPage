from pydantic import BaseModel

class Integration(BaseModel):
    name: str
    icon: str