from app.data.landing_data import integrations
from app.schemas.landing_schema.integration_schema import Integration


class IntegrationService:
    @staticmethod
    def get_all_integrations() -> list[Integration]:
        return [Integration(**item) for item in integrations]