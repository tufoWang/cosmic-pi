# src/services/space_resource_service.py

import requests

class SpaceResourceService:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def get_resources(self):
        """Fetches available space resources."""
        response = requests.get(f"{self.base_url}/resources", headers=self._get_headers())
        return self._handle_response(response)

    def allocate_resource(self, resource_id, amount):
        """Allocates a specified amount of a resource."""
        payload = {
            'resource_id': resource_id,
            'amount': amount
        }
        response = requests.post(f"{self.base_url}/resources/allocate", json=payload, headers=self._get_headers())
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
