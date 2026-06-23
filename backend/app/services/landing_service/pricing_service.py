from sqlalchemy.orm import Session

from app.models.landing_model.pricing_model import Pricing


def get_all_pricing(db: Session):
    return db.query(Pricing).all()


def get_pricing_by_id(
    db: Session,
    pricing_id: int
):
    return (
        db.query(Pricing)
        .filter(
            Pricing.id == pricing_id
        )
        .first()
    )


def create_pricing(
    db: Session,
    pricing_data
):
    pricing = Pricing(
        tier=pricing_data.tier,
        monthly=pricing_data.monthly,
        annual=pricing_data.annual,
        description=pricing_data.description,
        features=pricing_data.features,
        popular=pricing_data.popular
    )

    db.add(pricing)

    db.commit()
    db.refresh(pricing)

    return pricing


def update_pricing(
    db: Session,
    pricing_id: int,
    pricing_data
):
    pricing = get_pricing_by_id(
        db,
        pricing_id
    )

    if not pricing:
        return None

    pricing.tier = pricing_data.tier
    pricing.monthly = pricing_data.monthly
    pricing.annual = pricing_data.annual
    pricing.description = pricing_data.description
    pricing.features = pricing_data.features
    pricing.popular = pricing_data.popular

    db.commit()
    db.refresh(pricing)

    return pricing


def delete_pricing(
    db: Session,
    pricing_id: int
):
    pricing = get_pricing_by_id(
        db,
        pricing_id
    )

    if not pricing:
        return False

    db.delete(pricing)

    db.commit()

    return True