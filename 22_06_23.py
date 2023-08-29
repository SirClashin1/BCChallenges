from __future__ import annotations
from beginnercodes.challenges import test


def safecracker(dial_position, turn):
    ans = [(dial_position - turn[0]) % 100]
    ans.append((ans[0] + turn[1]) % 100)
    ans.append((ans[1] - turn[2]) % 100)
    return ans


test(690, safecracker)
