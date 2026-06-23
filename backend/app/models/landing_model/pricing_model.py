from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Boolean

from sqlalchemy.dialects.postgresql import ARRAY

from app.database.database import Base


class Pricing(Base):
    __tablename__ = "pricing"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    tier = Column(
        String(100),
        nullable=False
    )

    monthly = Column(
        String(50),
        nullable=False
    )

    annual = Column(
        String(50),
        nullable=False
    )

    description = Column(
        Text,
        nullable=False
    )

    features = Column(
        ARRAY(Text),
        nullable=False
    )

    popular = Column(
        Boolean,
        default=False
    )