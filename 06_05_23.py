from __future__ import annotations
from beginnercodes.challenges import test


def battle(stats: dict[str, int]) -> str:
    round_number = 0
    pHP = stats['pHP']
    pATT = stats['pATT']
    pDEF = stats['pDEF']
    pPOT = stats['pPOT']
    mHP = stats['mHP']
    mATT = stats['mATT']
    mDEF = stats['mDEF']
    mDAM = (mATT*2) - pDEF
    pDAM = (pATT*2) - mDEF
    def is_end():
        return mHP <= 0 or pHP <= 0
    while not is_end():
        potion_used = False
        round_number += 1
        if (pPOT > 0 and pHP <= 10):
            pHP += 10
            pPOT -= 1
            potion_used = True
        if potion_used:
            pHP -= 0.5*mDAM
        else:
            mHP -= pDAM
            if mHP <= 0:
                return (f"Victory in {round_number} rounds")
            pHP -= mDAM
            if pHP <= 0:
                return (f"Game Over in {round_number} rounds")
    
        


test(658, battle)