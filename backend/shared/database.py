from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Get the absolute path to the backend directory
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_dir = os.path.join(backend_dir, 'shared', 'db')
os.makedirs(db_dir, exist_ok=True)

# Use SQLite file-based database with absolute path
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(db_dir, 'supply_chain.db')}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 