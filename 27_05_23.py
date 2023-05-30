from __future__ import annotations
from beginnercodes.challenges import test
import re

def can_complete(input_str, word):   
    pattern = '^' + '.*?'.join(list(input_str)) + '$'
    return bool(re.match(pattern, word))


test(672, can_complete)