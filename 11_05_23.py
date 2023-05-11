from __future__ import annotations
from beginnercodes.challenges import test
import numpy as np

def lower_triangle(matrix: list[list[int]]) -> list[list[int]]:
    arr = np.array(matrix)
    arr[np.triu_indices(len(matrix), 1)] = 0
    return arr.tolist()

test(661, lower_triangle)  

