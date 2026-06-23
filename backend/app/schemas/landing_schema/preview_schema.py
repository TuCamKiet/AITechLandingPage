from pydantic import BaseModel


class PreviewBase(BaseModel):
    quote: str
    author: str
    role: str


class PreviewCreate(PreviewBase):
    pass


class PreviewUpdate(PreviewBase):
    pass


class PreviewResponse(PreviewBase):
    id: int

    model_config = {
        "from_attributes": True
    }