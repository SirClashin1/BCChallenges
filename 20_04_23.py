from __future__ import annotations
from beginnercodes.challenges import test

def tweak_letters(word: str, shift: list[int]) -> str:
    ans = ''
    for i, c in enumerate(word):
        if shift[i] == 0:
                ans += c
        if shift[i] == 1:
            ans += 'a' if c == 'z' else chr(ord(c) + 1)
        elif shift[i] == -1:
            ans += 'z' if c == 'a' else chr(ord(c) - 1)
    return ''.join(ans)

test(647, tweak_letters)
