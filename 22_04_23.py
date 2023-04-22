from __future__ import annotations
from beginnercodes.challenges import test


def three_sum(numbers: list[int]) -> list[list[int]]:
    ans = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                cur_l = [numbers[i], numbers[j], numbers[k]]
                if cur_l not in ans and sum(cur_l) == 0:
                    ans.append(cur_l)
            cur_l = []
    return ans

test(649, three_sum)



