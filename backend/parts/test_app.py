import unittest
from app import app

class TestPartsAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_part_success(self):
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
        
        # Check source location
        self.assertEqual(data['sourceLocation']['id'], '1')
        self.assertEqual(data['sourceLocation']['name'], 'Intel Factory')
        self.assertEqual(data['sourceLocation']['latitude'], 45.5155)
        self.assertEqual(data['sourceLocation']['longitude'], -122.6789)
        
        # Check supplier information
        self.assertEqual(len(data['suppliers']), 1)
        supplier = data['suppliers'][0]
        self.assertEqual(supplier['id'], '1')
        self.assertEqual(supplier['name'], 'Intel Corporation')
        self.assertEqual(supplier['address'], '2200 Mission College Blvd, Santa Clara, CA 95054')
        self.assertEqual(supplier['phone'], '+1 (408) 765-8080')
        self.assertEqual(supplier['email'], 'supplier.relations@intel.com')

if __name__ == '__main__':
    unittest.main() 