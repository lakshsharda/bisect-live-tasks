from taskkit.reports import summary
from taskkit.tasks import Task, TaskList


def make():
    tl = TaskList()
    tl.add(Task("pay rent", 3, "urgent"))
    tl.add(Task("water plants", 5))
    tl.add(Task("read book", 9, "low"))
    return tl


def test_summary_counts_overdue_and_due_today():
    assert summary(make(), 5) == "3 pending, 1 overdue, 1 due today"


def test_summary_when_everything_is_ahead():
    assert summary(make(), 0) == "3 pending, 0 overdue, 0 due today"


def test_summary_when_everything_is_late():
    assert summary(make(), 20) == "3 pending, 3 overdue, 0 due today"
