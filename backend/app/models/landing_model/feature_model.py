from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class Feature(Base):
    __tablename__ = "features"

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