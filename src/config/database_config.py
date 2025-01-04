# src/config/database_config.py

import os

class DatabaseConfig:
    """Database configuration settings."""
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '5432')
    DB_NAME = os.environ.get('DB_NAME', 'cosmic_pi')
    DB_USER = os.environ.get('DB_USER', 'your_db_user')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'your_db_password')

    @classmethod
    def get_connection_string(cls):
        """Returns the database connection string."""
        return f"postgresql://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"
