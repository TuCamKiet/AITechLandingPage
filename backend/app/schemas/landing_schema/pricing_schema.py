from pydantic import BaseModel
from typing import List


class PricingBase(BaseModel):
    tier: str
    monthly: str
    annual: str
    description: str
    features: List[str]
    popular: bool = False


class PricingCreate(PricingBase):
    pass


class PricingUpdate(PricingBase):
    pass


class PricingResponse(PricingBase):
    id: int

    model_config = {
        "from_attributes": True
    }