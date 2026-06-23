from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    icon = Column(
        String(100),
        nullable=False
    )

    name = Column(
        String(255),
        nullable=False
    )

    summary = Column(
        Text,
        nullable=False
    )