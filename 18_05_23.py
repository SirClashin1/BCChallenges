#Challenge 666, scary
from __future__ import annotations
from beginnercodes.challenges import test

def posneg(lst):
    if 0 in lst:
        return False
    def isneg(x):
        return x < 0
    lst = [isneg(x) for x in lst]
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return False
    return True


test(666, posneg)
