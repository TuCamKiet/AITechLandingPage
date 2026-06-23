from sqlalchemy.orm import Session

from app.models.landing_model.teammember_model import TeamMember


def get_all_team_members(db: Session):
    return db.query(TeamMember).all()


def get_team_member_by_id(
    db: Session,
    member_id: int
):
    return (
        db.query(TeamMember)
        .filter(
            TeamMember.id == member_id
        )
        .first()
    )


def create_team_member(
    db: Session,
    member_data
):
    member = TeamMember(
        name=member_data.name,
        role=member_data.role
    )

    db.add(member)

    db.commit()
    db.refresh(member)

    return member


def update_team_member(
    db: Session,
    member_id: int,
    member_data
):
    member = get_team_member_by_id(
        db,
        member_id
    )

    if not member:
        return None

    member.name = member_data.name
    member.role = member_data.role

    db.commit()
    db.refresh(member)

    return member


def delete_team_member(
    db: Session,
    member_id: int
):
    member = get_team_member_by_id(
        db,
        member_id
    )

    if not member:
        return False

    db.delete(member)

    db.commit()

    return True