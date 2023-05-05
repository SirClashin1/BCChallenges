from __future__ import annotations
from beginnercodes.challenges import test


def rep_set(values: int) -> list[list]:
    return [rep_set(val) for val in range(values)]


test(657, rep_set) 

