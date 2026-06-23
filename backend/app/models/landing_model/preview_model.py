from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class Preview(Base):
    __tablename__ = "previews"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    quote = Column(
        Text,
        nullable=False
    )

    author = Column(
        String(255),
        nullable=False
    )

    role = Column(
        String(255),
        nullable=False
    )