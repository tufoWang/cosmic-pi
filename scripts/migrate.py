# scripts/migrate.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_model_definitions import Base  # Import your SQLAlchemy Base

def migrate():
    """Run database migrations."""
    db_url = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)  # Create tables based on the defined models

    print("Database migration completed successfully.")

if __name__ == "__main__":
    migrate()
