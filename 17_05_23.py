from __future__ import annotations
from beginnercodes.challenges import test

def simple_pair(numbers: list[int], number: int) -> list[int] | None:
    if not numbers:
        return None

    first_num = numbers[0]
    remaining_nums = numbers[1:]
    
    for num in remaining_nums:
        if first_num * num == number:
            return [first_num, num]
    
    return simple_pair(remaining_nums, number)




test(665, simple_pair)  