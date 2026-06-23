from app.data.landing_data import pricing
from app.schemas.landing_schema.pricing_schema import Pricing


class PricingService:
    @staticmethod
    def get_all_pricing() -> list[Pricing]:
        return [Pricing(**item) for item in pricing]