import crud
import schemas


def ensure_created(task_step: schemas.TaskStepCreate):
    db_step = crud.task_step.get_by_name(task_step.name)
    if db_step:
        return db_step
    return crud.task_step.create(task_step)
