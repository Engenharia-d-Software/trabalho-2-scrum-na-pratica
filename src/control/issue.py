from sqlalchemy.exc import IntegrityError

import crud
from schemas import IssueCreate, IssueUpdate


def create_issue(issue: IssueCreate):
    try:
        return crud.issue.create(issue)
    except IntegrityError:
        pass

def update_issue(nome):
    issue = IssueUpdate(title=nome)
    try:
        crud.issue.update(issue)
    except IntegrityError:
        pass