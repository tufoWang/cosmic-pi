# tests/test_api.py

import unittest
from flask import Flask
from api.app import app

class TestAPIEndpoints(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_get_chain(self):
        """Test the /chain endpoint."""
        response = self.app.get('/chain')
        self.assertEqual(response.status_code, 200)
        self.assertIn('chain', response.get_json())

    def test_new_transaction(self):
        """Test the /transactions/new endpoint."""
        response = self.app.post('/transactions/new', json={
            'sender': 'Alice',
            'recipient': 'Bob',
            'amount': 50
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.get_json())

    def test_mine_block(self):
        """Test the /mine endpoint."""
        response = self.app.get('/mine')
        self.assertEqual(response.status_code, 200)
        self.assertIn('index', response.get_json())

if __name__ == '__main__':
    unittest.main()
