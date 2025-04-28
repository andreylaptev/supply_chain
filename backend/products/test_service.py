import unittest
from unittest.mock import Mock
from service import ProductService
from shared.models import Product, Part, ProductPart

class TestProductService(unittest.TestCase):
    def setUp(self):
        self.repository = Mock()
        self.service = ProductService(self.repository)

    def test_calculate_product_weight(self):
        # Create mock parts
        part1 = Mock(spec=Part)
        part1.weight = 1.0  # 1 kg
        
        part2 = Mock(spec=Part)
        part2.weight = 2.0  # 2 kg
        
        # Create mock product parts with quantities
        product_part1 = Mock(spec=ProductPart)
        product_part1.part = part1
        product_part1.quantity = 2  # 2 units of part1
        
        product_part2 = Mock(spec=ProductPart)
        product_part2.part = part2
        product_part2.quantity = 1  # 1 unit of part2
        
        # Create mock product
        product = Mock(spec=Product)
        product.parts = [product_part1, product_part2]
        
        # Calculate expected weight
        # sum_of_part_weights = (1.0 * 2) + (2.0 * 1) = 4.0
        # total_quantity = 2 + 1 = 3
        # weight = (4.0 * 1.15) + (3 * 0.3) + 0.75
        #        = 4.6 + 0.9 + 0.75
        #        = 6.25
        expected_weight = 6.25
        
        # Calculate actual weight
        actual_weight = self.service.calculate_product_weight(product)
        
        # Assert the result
        self.assertEqual(actual_weight, expected_weight)

if __name__ == '__main__':
    unittest.main() 