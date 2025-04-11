import unittest
from unittest.mock import patch, MagicMock
from app import app, get_product_repository

class TestProductsAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.get_product_repository')
    def test_get_products_returns_correct_data(self, mock_get_product_repository):
        mock_repo = MagicMock()
        mock_get_product_repository.return_value = mock_repo

        mock_product = MagicMock()
        mock_product.id = 1
        mock_product.name = "Test Product"
        mock_product.description = "Test Description"
        mock_product.total_cost = 100.0
        mock_product.delivery_time = "5 days"
        mock_product.assembly_location.id = 1
        mock_product.assembly_location.name = "Test Location"
        mock_product.assembly_location.latitude = 0.0
        mock_product.assembly_location.longitude = 0.0
        mock_part = MagicMock()
        mock_part.part.id = 1
        mock_part.part.name = "Test Part"
        mock_part.part.delivery_time = "3 days"
        mock_part.part.weight = 0.5
        mock_part.part.price = 50.0
        mock_part.part.source_location.id = 2
        mock_part.part.source_location.name = "Source Location"
        mock_part.part.source_location.latitude = 1.0
        mock_part.part.source_location.longitude = 1.0
        mock_product.parts = [mock_part]
        mock_repo.get_all_products.return_value = [mock_product]

        response = self.app.get('/api/products')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[0]['name'], "Test Product")
        self.assertEqual(data[0]['description'], "Test Description")
        self.assertEqual(data[0]['totalCost'], 100.0)
        self.assertEqual(data[0]['deliveryTime'], "5 days")
        self.assertEqual(data[0]['assemblyLocation']['id'], 1)
        self.assertEqual(data[0]['assemblyLocation']['name'], "Test Location")
        self.assertEqual(data[0]['assemblyLocation']['latitude'], 0.0)
        self.assertEqual(data[0]['assemblyLocation']['longitude'], 0.0)
        self.assertEqual(len(data[0]['parts']), 1)
        self.assertEqual(data[0]['parts'][0]['id'], 1)
        self.assertEqual(data[0]['parts'][0]['name'], "Test Part")
        self.assertEqual(data[0]['parts'][0]['deliveryTime'], "3 days")
        self.assertEqual(data[0]['parts'][0]['weight'], 0.5)
        self.assertEqual(data[0]['parts'][0]['price'], 50.0)
        self.assertEqual(data[0]['parts'][0]['sourceLocation']['id'], 2)
        self.assertEqual(data[0]['parts'][0]['sourceLocation']['name'], "Source Location")
        self.assertEqual(data[0]['parts'][0]['sourceLocation']['latitude'], 1.0)
        self.assertEqual(data[0]['parts'][0]['sourceLocation']['longitude'], 1.0)

    @patch('app.get_product_repository')
    def test_get_product_returns_correct_data(self, mock_get_product_repository):
        mock_repo = MagicMock()
        mock_get_product_repository.return_value = mock_repo

        mock_product = MagicMock()
        mock_product.id = 1
        mock_product.name = "Test Product"
        mock_product.description = "Test Description"
        mock_product.total_cost = 100.0
        mock_product.delivery_time = "5 days"
        mock_product.assembly_location.id = 1
        mock_product.assembly_location.name = "Test Location"
        mock_product.assembly_location.latitude = 0.0
        mock_product.assembly_location.longitude = 0.0
        mock_part = MagicMock()
        mock_part.part.id = 1
        mock_part.part.name = "Test Part"
        mock_part.part.delivery_time = "3 days"
        mock_part.part.weight = 0.5
        mock_part.part.price = 50.0
        mock_part.part.source_location.id = 2
        mock_part.part.source_location.name = "Source Location"
        mock_part.part.source_location.latitude = 1.0
        mock_part.part.source_location.longitude = 1.0
        mock_product.parts = [mock_part]
        mock_repo.get_product.return_value = mock_product

        response = self.app.get('/api/products/1')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['name'], "Test Product")
        self.assertEqual(data['description'], "Test Description")
        self.assertEqual(data['totalCost'], 100.0)
        self.assertEqual(data['deliveryTime'], "5 days")
        self.assertEqual(data['assemblyLocation']['id'], 1)
        self.assertEqual(data['assemblyLocation']['name'], "Test Location")
        self.assertEqual(data['assemblyLocation']['latitude'], 0.0)
        self.assertEqual(data['assemblyLocation']['longitude'], 0.0)
        self.assertEqual(len(data['parts']), 1)
        self.assertEqual(data['parts'][0]['id'], 1)
        self.assertEqual(data['parts'][0]['name'], "Test Part")
        self.assertEqual(data['parts'][0]['deliveryTime'], "3 days")
        self.assertEqual(data['parts'][0]['weight'], 0.5)
        self.assertEqual(data['parts'][0]['price'], 50.0)
        self.assertEqual(data['parts'][0]['sourceLocation']['id'], 2)
        self.assertEqual(data['parts'][0]['sourceLocation']['name'], "Source Location")
        self.assertEqual(data['parts'][0]['sourceLocation']['latitude'], 1.0)
        self.assertEqual(data['parts'][0]['sourceLocation']['longitude'], 1.0)

    @patch('app.get_product_repository')
    def test_get_product_not_found(self, mock_get_product_repository):
        mock_repo = MagicMock()
        mock_get_product_repository.return_value = mock_repo
        mock_repo.get_product.return_value = None

        response = self.app.get('/api/products/999')
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Product not found')

if __name__ == '__main__':
    unittest.main()
