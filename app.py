import os
def add_tax(amount, tax_rate):
    if amount < 0 or tax_rate < 0:
        raise ValueError("amount and tax_rate must be non-negative")
    return amount + (amount * tax_rate)
def get_api_key():
    return os.getenv("DEMO_API_KEY", "")

def order_total(price, quantity):
    if price < 0 or quantity <= 0:
        raise ValueError("price must be >= 0 and quantity must be > 0")
    return price * quantity
