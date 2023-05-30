from __future__ import annotations
from beginnercodes.challenges import test

def choose_fuse(fuse_ratings, device_current):
    return min((fuse for fuse in fuse_ratings if float(fuse[:-1]) >= float(device_current[:-1])),key=lambda x: float(x[:-1]))


test (673, choose_fuse)
