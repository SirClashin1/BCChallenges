from __future__ import annotations
from beginnercodes.challenges import test

def dice(lst):
    sum_lst = lst[0]
    for i in range(1, len(lst)):
        if lst[i-1] == 1:
            sum_lst -= lst[i]
        elif lst[i-1] == 6:
            sum_lst += lst[i]
        sum_lst += lst[i]
    return sum_lst

test(662, dice)