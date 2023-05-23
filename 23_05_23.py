from __future__ import annotations
from beginnercodes.challenges import test

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    elif a == 1 or b == 1:
        return max(a, b)
    
    lcm_value = max(a, b)
    while True:
        if lcm_value % a == 0 and lcm_value % b == 0:
            return lcm_value
        lcm_value += max(a, b)

test(669, lcm)