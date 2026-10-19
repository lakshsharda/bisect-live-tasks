"""Task priorities."""

LEVELS = {"low": 1, "normal": 2, "high": 3, "urgent": 4}


def level(name: str) -> int:
    try:
        return LEVELS[name.lower()]
    except KeyError:
        raise ValueError(f"unknown priority: {name!r}") from None


def sort_key(priority: str, due_day: int) -> tuple[int, int]:
    """Most urgent first, then the earliest due day."""
    return (-level(priority), due_day)
