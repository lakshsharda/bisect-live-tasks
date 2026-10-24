"""Tasks and the task list."""
from dataclasses import dataclass

from .dates import days_until, format_relative
from .priorities import level, sort_key


@dataclass
class Task:
    # Priorities are checked when a task is added to a list.
    title: str
    due_day: int
    priority: str = "normal"
    done: bool = False


class TaskList:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add(self, task: Task) -> None:
        if not task.title.strip():
            raise ValueError("a task needs a title")
        if task.due_day < 0:
            raise ValueError("due day cannot be negative")
        level(task.priority)
        self._tasks.append(task)

    def complete(self, title: str) -> None:
        for task in self._tasks:
            if task.title == title and not task.done:
                task.done = True
                return
        raise KeyError(title)

    def pending(self) -> list[Task]:
        return sorted((t for t in self._tasks if not t.done), key=lambda t: sort_key(t.priority, t.due_day))

    def overdue(self, today: int) -> list[Task]:
        return [t for t in self.pending() if days_until(t.due_day, today) < 0]

    def due_today(self, today: int) -> list[Task]:
        return [t for t in self.pending() if days_until(today, t.due_day) == 0]

    def titles(self) -> list[str]:
        return [t.title for t in self.pending()]


def is_high_priority(task: Task) -> bool:
    return level(task.priority) >= level("high")


def reminder_text(task: Task, today: int) -> str:
    """One-line reminder, e.g. 'pay rent: due in 3 day(s)'."""
    return f"{task.title}: {format_relative(days_until(today, task.due_day))}"
