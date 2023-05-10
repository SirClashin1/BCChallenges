from __future__ import annotations
from beginnercodes.challenges import test
from memory_profiler import profile

@profile
def gold_distribution(gold_piles: list[int]) -> list[int]:
    ans = [0, 0]
    left, right = 0, len(gold_piles) - 1
    while left <= right:
        if gold_piles[left] < gold_piles[right]:
            ans[(left + right + 1) % 2] += gold_piles[right]
            right -= 1
        else:
            ans[(left + right + 1) % 2] += gold_piles[left]
            left += 1
    return ans

test(660, gold_distribution)  
