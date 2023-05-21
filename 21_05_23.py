from __future__ import annotations
from beginnercodes.challenges import test

def diag_dom(matrix, idx=0):
    if idx >= len(matrix):
        return True
    diagonal_value = abs(matrix[idx][idx])
    rowsum = sum(abs(val) for i, val in enumerate(matrix[idx]) if i != idx)

    return False if diagonal_value <= rowsum else diag_dom(matrix, idx + 1)


test(668, diag_dom)