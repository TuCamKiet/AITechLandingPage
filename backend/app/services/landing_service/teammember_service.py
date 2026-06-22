from app.data.landing_data import teams
from app.schemas.landing_schema.teammenber_schema import TeamMember


class TeamMemberService:
    @staticmethod
    def get_all_teammembers() -> list[TeamMember]:
        return [TeamMember(**item) for item in teams]