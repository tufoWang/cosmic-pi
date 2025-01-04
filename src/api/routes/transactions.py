from flask import Blueprint, jsonify, request
from blockchain import Blockchain
from utils import validate_transaction

transactions_bp = Blueprint('transactions', __name__)
blockchain = Blockchain()

@transactions_bp.route('/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Validate transaction data
    if not validate_transaction(values):
        return jsonify({'error': 'Invalid transaction data'}), 400

    # Create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@transactions_bp.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = proof_of_work(last_proof)

    # Reward for finding the proof
    blockchain.new_transaction(
        sender="0",  # The sender is 0 to signify that this is a new coin
        recipient=request.remote_addr,
        amount=1,  # Reward amount can be adjusted as needed
    )

    # Create the new block
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200
