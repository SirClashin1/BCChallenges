from __future__ import annotations
from beginnercodes.challenges import test


def shift_letters(s):
    words = s.split(' ')
    if len(words) == 1:
        return s
    shifted_words = [words[-1][0] + words[0][1:]]
    shifted_words.extend(words[i - 1][0] + words[i][1:]
                         for i in range(1, len(words)))
    return ' '.join(shifted_words)


test(677, shift_letters)
