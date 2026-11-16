import pytest
from app import get_api_key, order_total
def test_order_total_rejects_zero_quantity():
    with pytest.raises(ValueError):
        order_total(100, 0)
def test_add_tax():
    from app import add_tax
    assert add_tax(100, 0.10) == 110

def test_order_total():
    assert order_total(100, 2) == 200

def test_order_total_rejects_invalid_quantity():
    with pytest.raises(ValueError):
        order_total(100, -1)

def test_api_key_defaults_to_empty(monkeypatch):
    monkeypatch.delenv("DEMO_API_KEY", raising=False)
    assert get_api_key() == ""
