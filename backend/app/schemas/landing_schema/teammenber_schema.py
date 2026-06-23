from pydantic import BaseModel


class TeamMemberBase(BaseModel):
    name: str
    role: str


class TeamMemberCreate(TeamMemberBase):
    pass


class TeamMemberUpdate(TeamMemberBase):
    pass


class TeamMemberResponse(TeamMemberBase):
    id: int

    model_config = {
        "from_attributes": True
    }