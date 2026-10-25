"""Text reports over a task list."""
from .dates import days_until, format_relative
from .tasks import TaskList


def summary(tasks: TaskList, today: int) -> str:
    return f"{len(tasks.pending())} pending, {len(tasks.overdue(today))} overdue, {len(tasks.due_today(today))} due today"


def agenda(tasks: TaskList, today: int) -> list[str]:
    return [f"{t.title}: {format_relative(days_until(today, t.due_day))}" for t in tasks.pending()]


def completed_line(done: int, total: int) -> str:
    return f"{done} of {total} done"
