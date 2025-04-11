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

if __name__ == '__main__':
    unittest.main() 