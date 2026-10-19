"""Day arithmetic. Days are integers (days since the project start)."""


def days_until(today: int, due: int) -> int:
    """Days from `today` until `due`; negative once the due day has passed."""
    return due - today


def format_relative(days: int) -> str:
    if days < 0:
        return f"{-days} day(s) overdue"
    if days == 0:
        return "due today"
    return f"due in {days} day(s)"
