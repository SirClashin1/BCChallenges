from __future__ import annotations
from beginnercodes.challenges import test

def missing(lst):
    return (len(lst) + 1) * (lst[0] + lst[-1]) / 2 - sum(lst)
        
test(671, missing)