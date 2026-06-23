from pydantic import BaseModel


class IntegrationBase(BaseModel):
    name: str
    icon: str


class IntegrationCreate(IntegrationBase):
    pass


class IntegrationUpdate(IntegrationBase):
    pass


class IntegrationResponse(IntegrationBase):
    id: int

    model_config = {
        "from_attributes": True
    }