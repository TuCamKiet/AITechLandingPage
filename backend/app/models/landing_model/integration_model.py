from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Integration(Base):
    __tablename__ = "integrations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(255),
        nullable=False
    )

    icon = Column(
        String(100),
        nullable=False
    )