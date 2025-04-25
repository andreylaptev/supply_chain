import unittest
from backend.shared.models import Product, ProductPart

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(total_cost=100.0)
        self.part1 = ProductPart(part=Product(total_cost=50.0), quantity=2)
        self.part2 = ProductPart(part=Product(total_cost=25.0), quantity=1)
        self.product.parts = [self.part1, self.part2]

    def test_calculate_price(self):
        expected_price = (50.0 * 2 + 25.0 * 1) * 1.25
        self.assertEqual(self.product.calculate_price(), expected_price)

if __name__ == '__main__':
    unittest.main()
