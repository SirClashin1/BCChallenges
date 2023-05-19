from __future__ import annotations
from beginnercodes.challenges import test
def is_prime(n):
    return False if n < 2 else all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def primebetween(a, b):
    if a > b:
        return False
    return True if is_prime(a) else primebetween(a + 1, b)

test(667, primebetween)
