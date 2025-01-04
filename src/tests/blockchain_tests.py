# src/tests/blockchain_tests.py

import unittest
from blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        """Set up a new blockchain instance for testing."""
        self.blockchain = Blockchain()

    def test_create_genesis_block(self):
        """Test that the genesis block is created correctly."""
        genesis_block = self.blockchain.chain[0]
        self.assertEqual(genesis_block['index'], 1)
        self.assertEqual(genesis_block['previous_hash'], '1')
        self.assertEqual(genesis_block['transactions'], [])
        self.assertIsNotNone(genesis_block['timestamp'])

    def test_add_transaction(self):
        """Test adding a transaction to the blockchain."""
        self.blockchain.new_transaction(sender="Alice", recipient="Bob", amount=50)
        self.assertEqual(len(self.blockchain.current_transactions), 1)
        self.assertEqual(self.blockchain.current_transactions[0]['sender'], "Alice")

    def test_mine_block(self):
        """Test mining a new block."""
        self.blockchain.new_transaction(sender="Alice", recipient="Bob", amount=50)
        previous_length = len(self.blockchain.chain)
        self.blockchain.mine()
        self.assertEqual(len(self.blockchain.chain), previous_length + 1)

if __name__ == '__main__':
    unittest.main()
