from __future__ import annotations
from beginnercodes.challenges import test

def encrypt(key , message):
    key = ' '.join([key[i:i+2] for i in range(0, len(key), 2)])
    for i,cm in enumerate(message):
        for j, ck in enumerate(key):
           if ck == cm:
                if key[j+1] != '' and j != len(key):
                    message[i] == key[j+1]
                elif key[j-1] != '' and j != 0:
                    message[i] == key[j-1]
                break
    return cm            

print(encrypt("ab c", "abc ab"))