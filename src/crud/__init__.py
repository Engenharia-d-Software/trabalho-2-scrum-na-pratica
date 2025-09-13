from model import Base

from .crud_task_step import CrudTaskStep
from .crud_issue import CrudIssue
from ._db import create_all, get_session


db_session = get_session()

task_step = CrudTaskStep(db_session)
issue = CrudIssue(db_session)
create_all(Base)
