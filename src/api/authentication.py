import jwt
import datetime
from flask import request, jsonify
from functools import wraps

SECRET_KEY = 'your_secret_key'  # Change this to a secure key in production

# In-memory user storage for demonstration purposes
users = {
    'user1': 'password1',  # Example user credentials
}

def generate_token(username):
    """Generates a JWT token for the user."""
    token = jwt.encode({
        'user': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }, SECRET_KEY, algorithm='HS256')
    return token

def authentication_middleware():
    """Middleware for user authentication using JWT."""
    token = None
    if 'Authorization' in request.headers:
        token = request.headers['Authorization'].split(" ")[1]

    if not token:
        return jsonify({'error': 'Token is missing!'}), 401

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        request.user = data['user']  # Store user info in request context
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired!'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token!'}), 401

def login_user(username, password):
    """Validates user credentials and returns a JWT token."""
    if username in users and users[username] == password:
        return generate_token(username)
    return None
