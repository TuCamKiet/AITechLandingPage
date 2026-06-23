from app.data.landing_data import showcases
from app.schemas.landing_schema.showcase_schema import Showcase


class ShowcaseService:
    @staticmethod
    def get_all_showcases() -> list[Showcase]:
        return [Showcase(**item) for item in showcases]