from app.data.landing_data import services
from app.schemas.landing_schema.service_schema import Service


class ServiceService:
    @staticmethod
    def get_all_services() -> list[Service]:
        return [Service(**item) for item in services]