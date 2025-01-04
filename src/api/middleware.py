from flask import Flask
from middleware.authentication import authentication_middleware
from middleware.rate_limiting import rate_limiting_middleware

def apply_middlewares(app: Flask):
    """Apply middleware functions to the Flask app."""
    app.before_request(authentication_middleware)
    app.before_request(rate_limiting_middleware)
