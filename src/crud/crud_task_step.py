from sqlalchemy.orm import Session

from model import TaskStep
from schemas import TaskStepCreate, TaskStepUpdate

from .crud import Crud


class CrudTaskStep(Crud[TaskStep, TaskStepCreate, TaskStepUpdate]):
    def __init__(self, db: Session):
        super().__init__(db, TaskStep)

    def get_by_name(self, name: str) -> TaskStep | None:
        stmt = self._db.query(TaskStep)
        stmt = stmt.filter(TaskStep.name == name)
        return stmt.first()
