"""Text reports over a task list."""
from .dates import days_until, format_relative
from .tasks import TaskList


def summary(tasks: TaskList, today: int) -> str:
    return f"{len(tasks.pending())} pending, {len(tasks.overdue(today))} overdue, {len(tasks.due_today(today))} due today"
