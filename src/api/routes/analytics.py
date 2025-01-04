from flask import Blueprint, jsonify

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/summary', methods=['GET'])
def get_summary():
    # Placeholder for analytics summary logic
    summary = {
        'total_transactions': 100,  # Example data
        'total_users': 50,          # Example data
        'total_resources': 2000,     # Example data
    }
    return jsonify(summary), 200
