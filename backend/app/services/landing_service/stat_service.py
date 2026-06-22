from app.data.landing_data import stats
from app.schemas.landing_schema.stat_schema import Stat


class StatService:
    @staticmethod
    def get_all_stats() -> list[Stat]:
        return [Stat(**item) for item in stats]