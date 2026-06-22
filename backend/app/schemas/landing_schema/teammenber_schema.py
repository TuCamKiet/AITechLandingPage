from pydantic import BaseModel
class TeamMember(BaseModel):
    name: str
    role: str