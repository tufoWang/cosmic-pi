# tests/test_integration.py

import unittest
from api.app import app
from blockchain import Blockchain

class TestIntegration(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client and a new blockchain instance."""
        self.app = app.test_client()
        self.app.testing = True
        self.blockchain = Blockchain()

    def test_full_transaction_flow(self):
        """Test the full flow of creating and mining a transaction."""
        # Create a new transaction
        response = self.app.post('/transactions/new', json={
            'sender': 'Alice',
            'recipient': 'Bob',
            'amount': 50
        })
        self.assertEqual(response.status_code, 201)

        # Mine the block
        response = self.app.get('/mine')
        self.assertEqual(response.status_code, 200)
        self.assertIn('index', response.get_json())

        # Check the blockchain for the new transaction
        self.assertEqual(len(self.blockchain.chain), 1)
        self.assertEqual(self.blockchain.chain[0]['transactions'][0]['sender'], 'Alice')

if __name__ == '__main__':
    unittest.main()
