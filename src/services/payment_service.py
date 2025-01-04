# src/services/payment_service.py

import requests

class PaymentService:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def create_payment(self, sender, recipient, amount):
        """Initiates a payment transaction."""
        payload = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        response = requests.post(f"{self.base_url}/payments", json=payload, headers=self._get_headers())
        return self._handle_response(response)

    def confirm_payment(self, payment_id):
        """Confirms a payment transaction."""
        response = requests.post(f"{self.base_url}/payments/{payment_id}/confirm", headers=self._get_headers())
        return self._handle_response(response)

    def _get_headers(self):
        """Returns the headers for API requests."""
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def _handle_response(self, response):
        """Handles API responses."""
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
