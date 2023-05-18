from __future__ import annotations
from beginnercodes.challenges import test

simple_pair = lambda arr, target: next(([x, y] for i, x in enumerate(arr) for y in arr[i+1:] if x * y == target), None)




test(665, simple_pair)  