import unittest
from backend.shared.models import Product, Part, ProductPart

class TestProductPriceCalculation(unittest.TestCase):
    def setUp(self):
        self.part1 = Part(id=1, name='Part 1', delivery_time='2 days', weight=1.0, price=100.0, source_location_id=1)
        self.part2 = Part(id=2, name='Part 2', delivery_time='3 days', weight=2.0, price=200.0, source_location_id=1)
        self.product = Product(id=1, name='Product 1', description='A test product', total_cost=300.0, delivery_time='5 days', assembly_location_id=1)
        self.product.parts = [ProductPart(product_id=1, part_id=1, quantity=2), ProductPart(product_id=1, part_id=2, quantity=1)]

    def test_calculate_price(self):
        expected_price = (2 * 100.0 + 1 * 200.0) * 1.25  # (parts_total) * (1 + markup_percentage)
        calculated_price = self.product.calculate_price()
        self.assertEqual(calculated_price, expected_price)

if __name__ == '__main__':
    unittest.main()
