from __future__ import annotations
from beginnercodes.challenges import test

def make_box(size: int) -> list[str]:
    ans = []
    for i in range(size):
        if i in [0, size - 1]:
            ans.append('#'*size)
        else:
            ans.append('#' + ' '*(size-2) + '#')
    return ans

test(648, make_box)