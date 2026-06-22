class Pricing(BaseModel):
    tier: str
    monthly: str
    annual: str
    description: str
    features: List[str]
    popular: Optional[bool] = False