# tests/test_frontend.py

import unittest
from frontend import app

class TestFrontend(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client for frontend testing."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test the home page loads correctly."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Cosmic Pi', response.data)

    def test_transaction_page(self):
        """Test the transaction page loads correctly."""
        response = self.app.get('/transaction')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Create a Transaction', response.data)

if __name__ == '__main__':
    unittest.main()
