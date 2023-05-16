from __future__ import annotations
from beginnercodes.challenges import test

def domino_chain(chain):
    if not chain:
        return ''
    chain = list(chain)
    for i, c in enumerate(chain):
        if c == '|':
            chain[i] = "/"
        else:
            break
    return ''.join(chain)

test(664, domino_chain)