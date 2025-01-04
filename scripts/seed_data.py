# scripts/seed_data.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_model_definitions import YourModel  # Import your SQLAlchemy models

def seed_data():
    """Seed the database with initial data."""
    db_url = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example of seeding data
    initial_data = [
        YourModel(name='Sample Data 1', value=100),
        YourModel(name='Sample Data 2', value=200),
    ]

    session.add_all(initial_data)
    session.commit()
    session.close()

    print("Database seeded with initial data successfully.")

if __name__ == "__main__":
    seed_data()
