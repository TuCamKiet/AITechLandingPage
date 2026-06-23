from pydantic import BaseModel
class FAQ(BaseModel):
    q: str
    a: str