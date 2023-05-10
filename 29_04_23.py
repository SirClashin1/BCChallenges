from __future__ import annotations
from beginnercodes.challenges import test
import math

def paths(x: int, y: int) -> int:
    return math.comb((x+y),x)

test(654, paths)