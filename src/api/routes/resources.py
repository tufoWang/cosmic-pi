from flask import Blueprint, jsonify

resources_bp = Blueprint('resources', __name__)

# In-memory resource storage (for demonstration purposes)
resources = {
    'water': 1000,
    'food': 500,
}

@resources_bp.route('/', methods=['GET'])
def get_resources():
    return jsonify(resources), 200

@resources_bp.route('/<resource_name>', methods=['GET'])
def get_resource(resource_name):
    resource_amount = resources.get(resource_name)
    if resource_amount is None:
        return jsonify({'error': 'Resource not found'}), 404

    return jsonify({resource_name: resource_amount}), 200
