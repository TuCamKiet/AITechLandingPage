from sqlalchemy.orm import Session

from app.models.landing_model.preview_model import Preview


def get_all_previews(db: Session):
    return db.query(Preview).all()


def get_preview_by_id(
    db: Session,
    preview_id: int
):
    return (
        db.query(Preview)
        .filter(
            Preview.id == preview_id
        )
        .first()
    )


def create_preview(
    db: Session,
    preview_data
):
    preview = Preview(
        quote=preview_data.quote,
        author=preview_data.author,
        role=preview_data.role
    )

    db.add(preview)

    db.commit()
    db.refresh(preview)

    return preview


def update_preview(
    db: Session,
    preview_id: int,
    preview_data
):
    preview = get_preview_by_id(
        db,
        preview_id
    )

    if not preview:
        return None

    preview.quote = preview_data.quote
    preview.author = preview_data.author
    preview.role = preview_data.role

    db.commit()
    db.refresh(preview)

    return preview


def delete_preview(
    db: Session,
    preview_id: int
):
    preview = get_preview_by_id(
        db,
        preview_id
    )

    if not preview:
        return False

    db.delete(preview)

    db.commit()

    return True