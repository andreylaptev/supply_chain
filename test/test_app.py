import unittest
from backend.shared.models import Product, ProductPart

class TestProductPriceCalculation(unittest.TestCase):

    def setUp(self):
        self.product = Product()
        self.product.parts = [
            ProductPart(part=MockPart(price=100), quantity=2),
            ProductPart(part=MockPart(price=50), quantity=3)
        ]

    def test_calculate_price(self):
        expected_price = (100 * 2 + 50 * 3) * 1.25
        self.assertEqual(self.product.calculate_price(), expected_price)

class MockPart:
    def __init__(self, price):
        self.price = price

if __name__ == '__main__':
    unittest.main()
