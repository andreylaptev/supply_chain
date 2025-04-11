import unittest
from app import app
from shared.database import get_db, engine
from shared.models import Base, Part, Location
from sqlalchemy.orm import Session

class TestPartsAPI(unittest.TestCase):
    def setUp(self):
        # Create test client
        self.app = app.test_client()
        self.app.testing = True
        
        # Create test database tables
        Base.metadata.create_all(bind=engine)
        
        # Create test data
        db = next(get_db())
        try:
            # Create test location
            location = Location(name="Test Factory", latitude=0.0, longitude=0.0)
            db.add(location)
            db.commit()
            
            # Create test part
            part = Part(
                name="Test CPU",
                delivery_time="5 days",
                weight=0.1,
                price=299.99,
                source_location_id=location.id
            )
            db.add(part)
            db.commit()
            
            self.test_part_id = part.id
        finally:
            db.close()

    def tearDown(self):
        # Clean up test database
        Base.metadata.drop_all(bind=engine)

    def test_get_part_returns_correct_data(self):
        response = self.app.get(f'/api/parts/{self.test_part_id}')
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], self.test_part_id)
        self.assertEqual(data['name'], 'Test CPU')
        self.assertEqual(data['deliveryTime'], '5 days')
        self.assertEqual(data['weight'], 0.1)
        self.assertEqual(data['price'], 299.99)

@patch('app.get_part_repository')
    def test_get_parts_returns_correct_data(self, mock_get_part_repository):
        mock_repo = MagicMock()
        mock_get_part_repository.return_value = mock_repo

        mock_part = MagicMock()
        mock_part.id = 1
        mock_part.name = "Test CPU"
        mock_part.delivery_time = "5 days"
        mock_part.weight = 0.1
        mock_part.price = 299.99
        mock_part.source_location.id = 1
        mock_part.source_location.name = "Test Factory"
        mock_part.source_location.latitude = 0.0
        mock_part.source_location.longitude = 0.0
        mock_part.suppliers = []

        mock_repo.get_all_parts.return_value = [mock_part]

        response = self.app.get('/api/parts')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[0]['name'], "Test CPU")
        self.assertEqual(data[0]['deliveryTime'], "5 days")
        self.assertEqual(data[0]['weight'], 0.1)
        self.assertEqual(data[0]['price'], 299.99)
        self.assertEqual(data[0]['sourceLocation']['id'], 1)
        self.assertEqual(data[0]['sourceLocation']['name'], "Test Factory")
        self.assertEqual(data[0]['sourceLocation']['latitude'], 0.0)
        self.assertEqual(data[0]['sourceLocation']['longitude'], 0.0)
        self.assertEqual(data[0]['suppliers'], [])

    @patch('app.get_part_repository')
    def test_get_part_returns_correct_data(self, mock_get_part_repository):
        mock_repo = MagicMock()
        mock_get_part_repository.return_value = mock_repo

        mock_part = MagicMock()
        mock_part.id = 1
        mock_part.name = "Test CPU"
        mock_part.delivery_time = "5 days"
        mock_part.weight = 0.1
        mock_part.price = 299.99
        mock_part.source_location.id = 1
        mock_part.source_location.name = "Test Factory"
        mock_part.source_location.latitude = 0.0
        mock_part.source_location.longitude = 0.0
        mock_part.suppliers = []

        mock_repo.get_part.return_value = mock_part

        response = self.app.get('/api/parts/1')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['name'], "Test CPU")
        self.assertEqual(data['deliveryTime'], "5 days")
        self.assertEqual(data['weight'], 0.1)
        self.assertEqual(data['price'], 299.99)
        self.assertEqual(data['sourceLocation']['id'], 1)
        self.assertEqual(data['sourceLocation']['name'], "Test Factory")
        self.assertEqual(data['sourceLocation']['latitude'], 0.0)
        self.assertEqual(data['sourceLocation']['longitude'], 0.0)
        self.assertEqual(data['suppliers'], [])

    @patch('app.get_part_repository')
    def test_get_part_returns_404_for_nonexistent_part(self, mock_get_part_repository):
        mock_repo = MagicMock()
        mock_get_part_repository.return_value = mock_repo

        mock_repo.get_part.return_value = None

        response = self.app.get('/api/parts/999')
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Part not found')

if __name__ == '__main__':
    unittest.main() 