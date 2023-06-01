from __future__ import annotations
from beginnercodes.challenges import test


def items_purchase(store, wallet):
    amm = int(wallet[1:].replace(",", ""))
    items = [item for item, price in store.items() if int(
        price[1:].replace(',', '')) <= amm]
    return sorted(items) if items else "Nothing"


test(675, items_purchase)
