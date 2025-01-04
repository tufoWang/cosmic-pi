# src/config/config.py

import os

class Config:
    """Base configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    API_BASE_URL = os.environ.get('API_BASE_URL', 'http://localhost:5000/api')
    PAYMENT_SERVICE_URL = os.environ.get('PAYMENT_SERVICE_URL', 'https://api.paymentservice.com')
    SPACE_RESOURCE_SERVICE_URL = os.environ.get('SPACE_RESOURCE_SERVICE_URL', 'https://api.spaceresource.com')
    NOTIFICATION_SERVICE_URL = os.environ.get('NOTIFICATION_SERVICE_URL', 'https://api.notificationservice.com')
    ANALYTICS_SERVICE_URL = os.environ.get('ANALYTICS_SERVICE_URL', 'https://api.analyticsservice.com')
    ORACLE_SERVICE_URL = os.environ.get('ORACLE_SERVICE_URL', 'https://api.oracle.com')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False

# You can add more configurations (e.g., TestingConfig) as needed
