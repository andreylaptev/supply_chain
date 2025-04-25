import unittest
from backend.shared.models import Product, ProductPart

class TestProductModel(unittest.TestCase):
    def setUp(self):
        self.product = Product(parts=[ProductPart(part=Part(price=10.0), quantity=2), ProductPart(part=Part(price=5.0), quantity=3)])

    def test_calculate_price(self):
        expected_price = (10.0 * 2 + 5.0 * 3) * 1.25
        self.assertEqual(self.product.calculate_price(), expected_price)

class Part:
    def __init__(self, price):
        self.price = price

if __name__ == '__main__':
    unittest.main()
