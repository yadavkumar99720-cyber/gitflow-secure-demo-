import os

def get_api_key():
    return os.getenv("DEMO_API_KEY", "")

def order_total(price, quantity):
    if price < 0 or quantity <= 0:
        raise ValueError("price must be >= 0 and quantity must be > 0")
    return price * quantity
