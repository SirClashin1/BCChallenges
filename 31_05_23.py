from __future__ import annotations
from beginnercodes.challenges import test

def has_valid_price(product):
    return bool(product and isinstance(product.get("price"), (int, float)) and product["price"] >= 0)

test(674, has_valid_price)
