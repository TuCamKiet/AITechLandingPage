from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Stat(Base):
    __tablename__ = "stats"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    label = Column(
        String(255),
        nullable=False,
    )

    value = Column(
        String(50),
        nullable=False,
    )