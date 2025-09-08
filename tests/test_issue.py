from datetime import datetime, timedelta

import crud
from schemas import IssueCreate, TaskStepCreate


def test_issue_is_created_with_correct_date():
    # arrange
    task_step = TaskStepCreate(name="test")
    db_task_step = crud.task_step.create(task_step)
    now = datetime.now().replace(microsecond=0, second=0)

    # act
    db_issue = crud.issue.create(
        IssueCreate(title="test", description="test", task_step_id=db_task_step.id)
    )
    created_at = db_issue.created_at.replace(microsecond=0, second=0)

    # assert
    assert now == created_at


def test_sorting_by_milestone():
    """
    This test are ment to test if the sorting by milestone crud method is correctly working.
    When called, the method should return the issues sorted by milestone attribute ascending, and
    should consider any issue with no milestone specified as bigger than issues with milestone specified.

    Example:

        given the following issues:
            [Issue(milestone=tomorrow), Issue(milestone=today), Issue(milestone=None)]

        The ordering should be:
            [Issue(milestone=today), Issue(milestone=tomorrow), Issue(milestone=None)]
    """
    # arrange
    db_task_step = crud.task_step.create(TaskStepCreate(name="test"))
    interval_between = timedelta(days=1)
    milestones: list[datetime | None] = [
        datetime.now() + interval_between,
        datetime.now(),
        datetime.now() - interval_between,
        None,
    ]
    for i, milestone in enumerate(milestones):
        crud.issue.create(
            IssueCreate(
                title=f"test_{i}",
                description="test",
                task_step_id=db_task_step.id,
                milestone=milestone,
            )
        )

    # arrange
    sorting_by_created_at = crud.issue.get_sorting_by_milestone(db_task_step.id)

    # assert
    title_names_sorted = ["test_2", "test_1", "test_0", "test_3"]
    assert [issue.title for issue in sorting_by_created_at] == title_names_sorted
