import unittest
from unittest.mock import MagicMock
from backend.shared.models import Product, Part, ProductPart, Location, Supplier

class TestProductPriceCalculation(unittest.TestCase):
    def setUp(self):
        self.part1 = Part(id=1, name='Part 1', delivery_time='2 days', weight=1.0, price=100.0, source_location_id=1)
        self.part2 = Part(id=2, name='Part 2', delivery_time='3 days', weight=2.0, price=200.0, source_location_id=1)
        self.product = Product(id=1, name='Product 1', description='A test product', total_cost=300.0, delivery_time='5 days', assembly_location_id=1)
        self.product.parts = [ProductPart(product_id=1, part_id=1, quantity=2), ProductPart(product_id=1, part_id=2, quantity=1)]

    def test_calculate_price(self):
        expected_price = 300.0 * 1.2  # total_cost * (1 + markup_percentage)
        calculated_price = self.product.calculate_price()
        self.assertEqual(calculated_price, expected_price)

class TestLocationModel(unittest.TestCase):
    def test_location_creation(self):
        location = Location(id=1, name='Location 1', latitude=12.34, longitude=56.78)
        self.assertEqual(location.id, 1)
        self.assertEqual(location.name, 'Location 1')
        self.assertEqual(location.latitude, 12.34)
        self.assertEqual(location.longitude, 56.78)

class TestSupplierModel(unittest.TestCase):
    def test_supplier_creation(self):
        supplier = Supplier(id=1, name='Supplier 1', address='123 Street', phone='1234567890', email='supplier@example.com', location_id=1)
        self.assertEqual(supplier.id, 1)
        self.assertEqual(supplier.name, 'Supplier 1')
        self.assertEqual(supplier.address, '123 Street')
        self.assertEqual(supplier.phone, '1234567890')
        self.assertEqual(supplier.email, 'supplier@example.com')
        self.assertEqual(supplier.location_id, 1)

class TestPartModel(unittest.TestCase):
    def test_part_creation(self):
        part = Part(id=1, name='Part 1', delivery_time='2 days', weight=1.0, price=100.0, source_location_id=1)
        self.assertEqual(part.id, 1)
        self.assertEqual(part.name, 'Part 1')
        self.assertEqual(part.delivery_time, '2 days')
        self.assertEqual(part.weight, 1.0)
        self.assertEqual(part.price, 100.0)
        self.assertEqual(part.source_location_id, 1)

class TestProductPartModel(unittest.TestCase):
    def test_product_part_creation(self):
        product_part = ProductPart(product_id=1, part_id=1, quantity=2)
        self.assertEqual(product_part.product_id, 1)
        self.assertEqual(product_part.part_id, 1)
        self.assertEqual(product_part.quantity, 2)

if __name__ == '__main__':
    unittest.main()
