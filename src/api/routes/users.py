from flask import Blueprint, jsonify, request

users_bp = Blueprint('users', __name__)

# In-memory user storage (for demonstration purposes)
users = {}

@users_bp.route('/register', methods=['POST'])
def register_user():
    values = request.get_json()
    username = values.get('username')
    password = values.get('password')

    if username in users:
        return jsonify({'error': 'User  already exists'}), 400

    users[username] = password  # Store user credentials (hashing recommended)
    return jsonify({'message': 'User  registered successfully'}), 201

@users_bp.route('/login', methods=['POST'])
def login_user():
    values = request.get_json()
    username = values.get('username')
    password = values.get('password')

    if username not in users or users[username] != password:
        return jsonify({'error': 'Invalid credentials'}), 401

    return jsonify({'message': 'Login successful'}), 200
