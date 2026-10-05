import pytest
from src.services.pricing_service import PricingService

def test_calculate_unit_price():
    assert PricingService.calculate_unit_price(2.5, 4) == 10.0

def test_calculate_weight_price():
    assert PricingService.calculate_weight_price(5.0, 2.2) == 11.0

def test_negative_unit_price_raise_error():
    with pytest.raises(ValueError):
        PricingService.calculate_unit_price(-1, 5)

def test_negative_weight_raise_error():
    with pytest.raises(ValueError):
        PricingService.calculate_weight_price(3, -0.5)
