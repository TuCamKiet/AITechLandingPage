from app.data.landing_data import features
from app.schemas.landing_schema.feature_schema import Feature


class FeatureService:
    @staticmethod
    def get_all_features() -> list[Feature]:
        return [Feature(**item) for item in features]