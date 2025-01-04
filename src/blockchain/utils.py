import hashlib
import json
from time import time

def hash_block(block):
    """Creates a SHA-256 hash of a block."""
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

def validate_transaction(transaction):
    """Validates a transaction to ensure it has the required fields."""
    required_fields = ['sender', 'recipient', 'amount']
    return all(field in transaction for field in required_fields) and transaction['amount'] > 0

def create_genesis_block():
    """Creates the genesis block for the blockchain."""
    return {
        'index': 1,
        'timestamp': time(),
        'transactions': [],
        'proof': 100,  # Arbitrary proof for the genesis block
        'previous_hash': '1',  # Previous hash for the genesis block
    }

def format_timestamp(timestamp):
    """Formats a timestamp into a human-readable string."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

def calculate_transaction_fee(amount):
    """Calculates the transaction fee based on the amount."""
    fee_percentage = 0.01  # 1% transaction fee
    return amount * fee_percentage

def is_valid_chain(chain):
    """Validates the entire blockchain to ensure integrity."""
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i - 1]

        # Check if the previous hash is correct
        if current_block['previous_hash'] != hash_block(previous_block):
            return False

        # Check if the current block's transactions are valid
        for transaction in current_block['transactions']:
            if not validate_transaction(transaction):
                return False

    return True
