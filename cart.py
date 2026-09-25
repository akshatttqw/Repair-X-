from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float
    quantity: int = 1

def calculate_total(items):
    # INTENTIONAL DEMO BUG:
    # quantity is ignored when calculating the total.
    return sum(item.price for item in items)
