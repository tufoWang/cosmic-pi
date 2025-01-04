from flask import Flask, jsonify, request
from blockchain import Blockchain
from utils import validate_transaction, create_genesis_block
from constants import PI_COIN_VALUE

app = Flask(__name__)

# Create a new instance of the Blockchain
blockchain = Blockchain()

# Initialize the blockchain with a genesis block
blockchain.chain.append(create_genesis_block())

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST data
    if not validate_transaction(values):
        return jsonify({'error': 'Invalid transaction data'}), 400

    # Create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
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

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()
    nodes = values.get('nodes')

    if nodes is None:
        return jsonify({'error': 'Error: Please supply a valid list of nodes'}), 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain,
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain,
        }

    return jsonify(response), 200

def proof_of_work(last_proof):
    proof = 0
    while not valid_proof(last_proof, proof):
        proof += 1
    return proof

def valid_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"  # The proof must be a hash that starts with four zeros

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
