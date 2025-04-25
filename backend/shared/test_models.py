import unittest
from unittest.mock import MagicMock
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Location, Supplier, Part, Product, ProductPart

class TestLocation(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_location_creation(self):
        location = Location(name="Warehouse", latitude=40.7128, longitude=-74.0060)
        self.session.add(location)
        self.session.commit()
        retrieved_location = self.session.query(Location).filter_by(name="Warehouse").first()
        self.assertIsNotNone(retrieved_location)
        self.assertEqual(retrieved_location.latitude, 40.7128)
        self.assertEqual(retrieved_location.longitude, -74.0060)

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_supplier_creation(self):
        location = Location(name="Warehouse", latitude=40.7128, longitude=-74.0060)
        self.session.add(location)
        self.session.commit()
        supplier = Supplier(name="Supplier A", address="123 Main St", phone="555-1234", email="supplier@example.com", location_id=location.id)
        self.session.add(supplier)
        self.session.commit()
        retrieved_supplier = self.session.query(Supplier).filter_by(name="Supplier A").first()
        self.assertIsNotNone(retrieved_supplier)
        self.assertEqual(retrieved_supplier.address, "123 Main St")
        self.assertEqual(retrieved_supplier.phone, "555-1234")
        self.assertEqual(retrieved_supplier.email, "supplier@example.com")
        self.assertEqual(retrieved_supplier.location_id, location.id)

class TestPart(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_part_creation(self):
        location = Location(name="Warehouse", latitude=40.7128, longitude=-74.0060)
        self.session.add(location)
        self.session.commit()
        part = Part(name="Part A", delivery_time="2 days", weight=1.5, price=100.0, source_location_id=location.id)
        self.session.add(part)
        self.session.commit()
        retrieved_part = self.session.query(Part).filter_by(name="Part A").first()
        self.assertIsNotNone(retrieved_part)
        self.assertEqual(retrieved_part.delivery_time, "2 days")
        self.assertEqual(retrieved_part.weight, 1.5)
        self.assertEqual(retrieved_part.price, 100.0)
        self.assertEqual(retrieved_part.source_location_id, location.id)

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_product_creation(self):
        location = Location(name="Factory", latitude=34.0522, longitude=-118.2437)
        self.session.add(location)
        self.session.commit()
        product = Product(name="Product A", description="A sample product", total_cost=500.0, delivery_time="5 days", assembly_location_id=location.id)
        self.session.add(product)
        self.session.commit()
        retrieved_product = self.session.query(Product).filter_by(name="Product A").first()
        self.assertIsNotNone(retrieved_product)
        self.assertEqual(retrieved_product.description, "A sample product")
        self.assertEqual(retrieved_product.total_cost, 500.0)
        self.assertEqual(retrieved_product.delivery_time, "5 days")
        self.assertEqual(retrieved_product.assembly_location_id, location.id)

    def test_calculate_price(self):
        product = Product(name="Product A", description="A sample product", total_cost=500.0, delivery_time="5 days")
        calculated_price = product.calculate_price()
        self.assertEqual(calculated_price, 600.0)  # 500 * 1.2 = 600

class TestProductPart(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_product_part_creation(self):
        location = Location(name="Factory", latitude=34.0522, longitude=-118.2437)
        self.session.add(location)
        self.session.commit()
        product = Product(name="Product A", description="A sample product", total_cost=500.0, delivery_time="5 days", assembly_location_id=location.id)
        self.session.add(product)
        self.session.commit()
        part = Part(name="Part A", delivery_time="2 days", weight=1.5, price=100.0, source_location_id=location.id)
        self.session.add(part)
        self.session.commit()
        product_part = ProductPart(product_id=product.id, part_id=part.id, quantity=10)
        self.session.add(product_part)
        self.session.commit()
        retrieved_product_part = self.session.query(ProductPart).filter_by(product_id=product.id, part_id=part.id).first()
        self.assertIsNotNone(retrieved_product_part)
        self.assertEqual(retrieved_product_part.quantity, 10)

if __name__ == '__main__':
    unittest.main()