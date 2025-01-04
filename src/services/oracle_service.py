src/services/oracle_service.py

import requests

class OracleService:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def get_real_time_data(self, data_type):
        """Fetches real-time data from the oracle."""
        response = requests.get(f"{self.base_url}/oracle/data/{data_type}", headers=self._get_headers())
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
