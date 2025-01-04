from flask import Blueprint, jsonify

notifications_bp = Blueprint('notifications', __name__)

# In-memory notification storage (for demonstration purposes)
notifications = []

@notifications_bp.route('/', methods=['GET'])
def get_notifications():
    return jsonify(notifications), 200

@notifications_bp.route('/add', methods=['POST'])
def add_notification():
    values = request.get_json()
    message = values.get('message')

    notifications.append({'message : message})
    return jsonify({'message': 'Notification added successfully'}), 201
