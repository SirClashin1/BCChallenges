from __future__ import annotations
from beginnercodes.challenges import test


def round_n(n, fac):
    ans = (n // fac) * fac
    if n % fac >= fac // 2:
        ans += fac
    return ans


test(686, round_n)
