"""
Pricing Service for Greenhill Food Co-op
Supports per-unit pricing and per-weight(kg) pricing
"""

class PricingService:
    @staticmethod
    def calculate_unit_price(price_per_unit: float, quantity: int) -> float:
        """Calculate total price for items sold by unit"""
        if quantity < 0 or price_per_unit < 0:
            raise ValueError("Price and quantity cannot be negative")
        return price_per_unit * quantity

    @staticmethod
    def calculate_weight_price(price_per_kg: float, weight_kg: float) -> float:
        """Calculate total price for items sold by weight"""
        if weight_kg < 0 or price_per_kg < 0:
            raise ValueError("Price and weight cannot be negative")
        return price_per_kg * weight_kg
