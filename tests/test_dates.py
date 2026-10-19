from taskkit.dates import days_until, format_relative


def test_days_until_a_future_day():
    assert days_until(5, 8) == 3


def test_days_until_today_is_zero():
    assert days_until(5, 5) == 0


def test_days_until_is_negative_after_the_due_day():
    assert days_until(8, 5) == -3


def test_format_relative():
    assert format_relative(3) == "due in 3 day(s)"
    assert format_relative(0) == "due today"
    assert format_relative(-2) == "2 day(s) overdue"
