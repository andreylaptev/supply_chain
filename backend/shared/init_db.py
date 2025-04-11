from .base import Base
from .database import engine
from .models import Location, Part, Product, Supplier, ProductPart
from .seed import seed_database
from sqlalchemy import inspect

def init_db():
    try:
        print("Starting database initialization...")
        
        # Drop all tables first to ensure clean state
        print("Dropping existing tables...")
        Base.metadata.drop_all(bind=engine)
        
        # Create all tables
        print("Creating tables...")
        Base.metadata.create_all(bind=engine)
        
        # Verify tables were created
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"Created tables: {tables}")
        
        # Seed the database
        print("Seeding database...")
        seed_database()
        
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise

if __name__ == "__main__":
    init_db() 