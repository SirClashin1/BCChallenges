from __future__ import annotations
from beginnercodes.challenges import test
import re


def extract_mentions(msg):
    mentions = re.findall(r'[@#]\w+', msg)
    return ' '.join(mentions)


test(678, extract_mentions)
