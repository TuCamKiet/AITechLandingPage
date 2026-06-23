from pydantic import BaseModel


class FAQBase(BaseModel):
    q: str
    a: str


class FAQCreate(FAQBase):
    pass


class FAQUpdate(FAQBase):
    pass


class FAQResponse(FAQBase):
    id: int

    model_config = {
        "from_attributes": True
    }