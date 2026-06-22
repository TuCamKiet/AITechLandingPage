from pydantic import BaseModel
class Stat(BaseModel):
    label: str
    value: str
