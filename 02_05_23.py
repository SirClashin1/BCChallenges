from __future__ import annotations
from beginnercodes.challenges import test

def sum_two_smallest_nums(nums: list[int]) -> int:
   nums = [i for i in nums if i>0]
   return sum(sorted(nums)[:2])
test(655, sum_two_smallest_nums)