from __future__ import annotations
from beginnercodes.challenges import test


def is_there_consecutive(input_arr, num, count_of_num):
    current_count = 0
    for x in input_arr:
        current_count = current_count + 1 if x == num else 0
        if current_count == count_of_num:
            return True
    return count_of_num == 0 and current_count == 0


test(683, is_there_consecutive)
