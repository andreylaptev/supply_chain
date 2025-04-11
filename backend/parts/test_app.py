import unittest
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

    def test_get_part_not_found(self):
        # Test getting a non-existing part
        response = self.app.get('/api/parts/999')
        data = response.get_json()
        
        # Check response status code
        self.assertEqual(response.status_code, 404)
        
        # Check response data structure
        self.assertEqual(data['error'], 'Part not found')

    def test_get_all_parts(self):
        # Test getting all parts
        response = self.app.get('/api/parts')
        data = response.get_json()
        
        # Check response status code
        self.assertEqual(response.status_code, 200)
        
        # Check response data structure
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 8)
        
        # Check first part data
        self.assertEqual(data[0]['id'], '1')
        self.assertEqual(data[0]['name'], 'CPU')
        self.assertEqual(data[0]['deliveryTime'], '5 days')
        self.assertEqual(data[0]['weight'], 0.1)
        self.assertEqual(data[0]['price'], 299.99)

if __name__ == '__main__':
    unittest.main() 