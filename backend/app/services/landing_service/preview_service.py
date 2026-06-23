from app.data.landing_data import previews
from app.schemas.landing_schema.preview_schema import Preview


class PreviewService:
    @staticmethod
    def get_all_previews() -> list[Preview]:
        return [Preview(**item) for item in previews]