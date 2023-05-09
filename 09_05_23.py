from __future__ import annotations
from beginnercodes.challenges import test


def lottery(ticket: list[list[str | int]], win: int) -> str:
    wins = 0
    for code,num in ticket:
        for c in code:
            if ord(c)==num:
                wins+=1
                break
    return "Winner!" if wins>=win else "Loser!"
test(659, lottery) 