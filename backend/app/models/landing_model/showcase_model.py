from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class Showcase(Base):
    __tablename__ = "showcases"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    icon = Column(
        String(100),
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    description = Column(
        Text,
        nullable=False
    )

    metric = Column(
        String(100),
        nullable=False
    )