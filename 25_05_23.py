from __future__ import annotations
from beginnercodes.challenges import test

def num_rep(string):
    length = len(string)
    for i in range(1, length // 2 + 1):
        sub = string[:i]
        rep = length // len(sub)
        if sub * rep == string:
            return rep

    return 1
    

test(670, num_rep)
