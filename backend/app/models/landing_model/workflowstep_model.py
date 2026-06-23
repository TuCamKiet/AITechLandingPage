from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class WorkflowStep(Base):
    __tablename__ = "workflow_steps"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    step = Column(
        String(10),
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    detail = Column(
        Text,
        nullable=False
    )