# src/config/logging_config.py

import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging():
    """Sets up logging configuration."""
    log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()
    log_file = os.environ.get('LOG_FILE', 'app.log')

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5)
    handler.setLevel(log_level)

    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Get the root logger and set the handler
    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.addHandler(handler)

    # Optionally, log to console as well
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.info("Logging is set up.")
