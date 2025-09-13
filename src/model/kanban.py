from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

from .base import Base

class Issue(Base):
    __tablename__ = "issues"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str]
    created_at: Mapped[datetime]
    milestone: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    task_step_id: Mapped[int] = mapped_column(ForeignKey("task_steps.id"))
    task_step: Mapped[TaskStep] = relationship(back_populates="issues")


class TaskStep(Base):
    __tablename__ = "task_steps"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    wip_limit: Mapped[int | None] = mapped_column(nullable=True) # when null, it means that no wip limit were set

    issues: Mapped[list[Issue]] = relationship(back_populates="task_step")
