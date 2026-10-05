from src.services.order_service import OrderService

def test_order_total_calculation():
    order = OrderService()
    order.add_unit_item("Apple", 3, 2)
    order.add_weight_item("Potato", 4, 1.5)
    assert order.get_order_total() == 12
