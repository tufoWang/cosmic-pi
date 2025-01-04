# src/services/notification_service.py

import requests

class NotificationService:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def send_notification(self, user_id, message):
        """Sends a notification to a user."""
        payload = {
            'user_id': user_id,
            'message': message
        }
        response = requests.post(f"{self.base_url}/notifications", json=payload, headers=self._get_headers())
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
