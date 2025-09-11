from model import TaskStep, Base
from schemas import TaskStepCreate, TaskStepUpdate

from .crud import Crud
from .crud_issue import CrudIssue
from ._db import create_all, get_session


db_session = get_session()

task_step = Crud[TaskStep, TaskStepCreate, TaskStepUpdate](db_session, TaskStep)
issue = CrudIssue(db_session)
create_all(Base)
