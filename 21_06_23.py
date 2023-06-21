from __future__ import annotations
from beginnercodes.challenges import test


def trouble(num1, num2):
    str1, str2 = str(num1), str(num2)

    return any(str1[i] == str1[i + 1] == str1[i + 2] and str1[i] * 2 in str2 for i in range(len(str1) - 2))


test(689, trouble)
