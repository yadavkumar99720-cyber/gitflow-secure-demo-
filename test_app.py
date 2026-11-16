import pytest
from app import get_api_key, order_total

def test_order_total():
    assert order_total(100, 2) == 200

def test_order_total_rejects_invalid_quantity():
    with pytest.raises(ValueError):
        order_total(100, -1)

def test_api_key_defaults_to_empty(monkeypatch):
    monkeypatch.delenv("DEMO_API_KEY", raising=False)
    assert get_api_key() == ""
