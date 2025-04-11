import unittest
from unittest.mock import patch, MagicMock
from app import app

class TestPartsAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_part_returns_correct_data(self):
        # Test getting an existing part (CPU)
        response = self.app.get('/api/parts/1')
        data = response.get_json()
        
        # Check response status code
        self.assertEqual(response.status_code, 200)
        
        # Check response data structure
        self.assertEqual(data['id'], '1')
        self.assertEqual(data['name'], 'CPU')
        self.assertEqual(data['deliveryTime'], '5 days')
        self.assertEqual(data['weight'], 0.1)
        self.assertEqual(data['price'], 299.99)

    @patch('app.get_part_repository')
    def test_get_parts_returns_correct_data(self, mock_get_part_repository):
        # Mock the repository and its return value
        mock_repo = MagicMock()
        mock_repo.get_all_parts.return_value = [
            MagicMock(
                id='1',
                name='CPU',
                delivery_time='5 days',
                weight=0.1,
                price=299.99,
                source_location=MagicMock(
                    id='1',
                    name='Warehouse A',
                    latitude=40.7128,
                    longitude=-74.0060
                ),
                suppliers=[
                    MagicMock(
                        id='1',
                        name='Supplier A',
                        address='123 Main St',
                        phone='123-456-7890',
                        email='supplierA@example.com',
                        location=MagicMock(
                            id='1',
                            name='Location A',
                            latitude=40.7128,
                            longitude=-74.0060
                        )
                    )
                ]
            )
        ]
        mock_get_part_repository.return_value = mock_repo

        response = self.app.get('/api/parts')
        data = response.get_json()

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check response data structure
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], '1')
        self.assertEqual(data[0]['name'], 'CPU')
        self.assertEqual(data[0]['deliveryTime'], '5 days')
        self.assertEqual(data[0]['weight'], 0.1)
        self.assertEqual(data[0]['price'], 299.99)
        self.assertEqual(data[0]['sourceLocation']['id'], '1')
        self.assertEqual(data[0]['sourceLocation']['name'], 'Warehouse A')
        self.assertEqual(data[0]['sourceLocation']['latitude'], 40.7128)
        self.assertEqual(data[0]['sourceLocation']['longitude'], -74.0060)
        self.assertEqual(len(data[0]['suppliers']), 1)
        self.assertEqual(data[0]['suppliers'][0]['id'], '1')
        self.assertEqual(data[0]['suppliers'][0]['name'], 'Supplier A')
        self.assertEqual(data[0]['suppliers'][0]['address'], '123 Main St')
        self.assertEqual(data[0]['suppliers'][0]['phone'], '123-456-7890')
        self.assertEqual(data[0]['suppliers'][0]['email'], 'supplierA@example.com')
        self.assertEqual(data[0]['suppliers'][0]['location']['id'], '1')
        self.assertEqual(data[0]['suppliers'][0]['location']['name'], 'Location A')
        self.assertEqual(data[0]['suppliers'][0]['location']['latitude'], 40.7128)
        self.assertEqual(data[0]['suppliers'][0]['location']['longitude'], -74.0060)

    @patch('app.get_part_repository')
    def test_get_part_not_found(self, mock_get_part_repository):
        # Mock the repository and its return value
        mock_repo = MagicMock()
        mock_repo.get_part.return_value = None
        mock_get_part_repository.return_value = mock_repo

        response = self.app.get('/api/parts/999')
        data = response.get_json()

        # Check response status code
        self.assertEqual(response.status_code, 404)

        # Check response data structure
        self.assertEqual(data['error'], 'Part not found')

if __name__ == '__main__':
    unittest.main() 