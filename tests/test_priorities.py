import pytest

from taskkit.priorities import level, sort_key


def test_levels_are_ordered():
    assert level("low") < level("normal") < level("high") < level("urgent")


def test_names_ignore_case():
    assert level("HIGH") == 3


def test_unknown_priority_is_rejected():
    with pytest.raises(ValueError):
        level("whenever")


def test_more_urgent_sorts_first():
    assert sort_key("urgent", 9) < sort_key("normal", 1)


def test_same_priority_sorts_by_due_day():
    assert sort_key("high", 2) < sort_key("high", 5)
