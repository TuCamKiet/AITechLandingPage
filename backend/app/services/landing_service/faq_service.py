from sqlalchemy.orm import Session

from app.models.landing_model.faq_model import FAQ


def get_all_faqs(db: Session):
    return db.query(FAQ).all()


def get_faq_by_id(
    db: Session,
    faq_id: int
):
    return (
        db.query(FAQ)
        .filter(
            FAQ.id == faq_id
        )
        .first()
    )


def create_faq(
    db: Session,
    faq_data
):
    faq = FAQ(
        q=faq_data.q,
        a=faq_data.a
    )

    db.add(faq)

    db.commit()
    db.refresh(faq)

    return faq


def update_faq(
    db: Session,
    faq_id: int,
    faq_data
):
    faq = get_faq_by_id(
        db,
        faq_id
    )

    if not faq:
        return None

    faq.q = faq_data.q
    faq.a = faq_data.a

    db.commit()
    db.refresh(faq)

    return faq


def delete_faq(
    db: Session,
    faq_id: int
):
    faq = get_faq_by_id(
        db,
        faq_id
    )

    if not faq:
        return False

    db.delete(faq)

    db.commit()

    return True