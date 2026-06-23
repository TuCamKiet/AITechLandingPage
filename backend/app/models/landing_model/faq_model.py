from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text

from app.database.database import Base


class FAQ(Base):
    __tablename__ = "faqs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    q = Column(
        Text,
        nullable=False
    )

    a = Column(
        Text,
        nullable=False
    )