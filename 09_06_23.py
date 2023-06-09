from __future__ import annotations
from beginnercodes.challenges import test


def weekly_salary(hours):
    return sum((h * 10 if h <= 8 else 80 + (h - 8) * 15) if i < 5 else (2 * (h * 10 if h <= 8 else 80 + (h - 8) * 15)) for i, h in enumerate(hours))


test(681, weekly_salary)
