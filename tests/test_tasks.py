import pytest

from taskkit.tasks import Task, TaskList


def make():
    tl = TaskList()
    tl.add(Task("pay rent", 3, "urgent"))
    tl.add(Task("water plants", 5))
    tl.add(Task("read book", 9, "low"))
    return tl


def test_pending_is_sorted_by_priority_then_day():
    assert [t.title for t in make().pending()] == ["pay rent", "water plants", "read book"]


def test_complete_removes_a_task_from_pending():
    tl = make()
    tl.complete("pay rent")
    assert [t.title for t in tl.pending()] == ["water plants", "read book"]


def test_completing_an_unknown_task_fails():
    with pytest.raises(KeyError):
        make().complete("nope")


def test_a_task_needs_a_title():
    with pytest.raises(ValueError):
        TaskList().add(Task("  ", 1))


def test_due_day_cannot_be_negative():
    with pytest.raises(ValueError):
        TaskList().add(Task("x", -1))


def test_unknown_priority_is_rejected():
    with pytest.raises(ValueError):
        TaskList().add(Task("x", 1, "whenever"))
