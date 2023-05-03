from __future__ import annotations
from typing import Any
from beginnercodes.challenges import test


def flick_switch(values: list[Any]) -> list[bool]:
    ans = [True] * len(values)
    bval = True
    for i, val in enumerate(values):
        if val == "flick":
            bval = not bval
            ans[i:] = [bval] * (len(values)-i)
    return ans
test(656, flick_switch)