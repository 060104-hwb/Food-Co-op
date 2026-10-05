"""
Order Service for Greenhill Food Co-op
Handle order creation, item aggregation and order total calculation
"""
from src.services.pricing_service import PricingService

class OrderService:
    def __init__(self):
        self.order_items = []

    def add_unit_item(self, name: str, price_per_unit: float, quantity: int):
        total = PricingService.calculate_unit_price(price_per_unit, quantity)
        self.order_items.append({"name": name, "total": total})

    def add_weight_item(self, name: str, price_per_kg: float, weight_kg: float):
        total = PricingService.calculate_weight_price(price_per_kg, weight_kg)
        self.order_items.append({"name": name, "total": total})

    def get_order_total(self) -> float:
        return sum(item["total"] for item in self.order_items)
