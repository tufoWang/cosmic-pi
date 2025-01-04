# src/services/analytics_service.py

import requests

class AnalyticsService:
    def __init__(self, api_key, base_url):
        """
        Initializes the AnalyticsService with the provided API key and base URL.

        :param api_key: API key for authentication with the analytics service
        :param base_url: Base URL of the analytics API
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_user_activity(self, user_id):
        """
        Fetches user activity data for a specific user.

        :param user_id: The ID of the user whose activity data is to be fetched
        :return: JSON response containing user activity data
        """
        response = requests.get(f"{self.base_url}/analytics/user/{user_id}", headers=self._get_headers())
        return self._handle_response(response)

    def get_transaction_stats(self):
        """
        Fetches statistics on transactions.

        :return: JSON response containing transaction statistics
        """
        response = requests.get(f"{self.base_url}/analytics/transactions", headers=self._get_headers())
        return self._handle_response(response)

    def get_system_health(self):
        """
        Fetches the health status of the analytics system.

        :return: JSON response containing system health information
        """
        response = requests.get(f"{self.base_url}/analytics/health", headers=self._get_headers())
        return self._handle_response(response)

    def _get_headers(self):
        """
        Returns the headers for API requests.

        :return: Dictionary containing authorization and content type headers
        """
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def _handle_response(self, response):
        """
        Handles API responses and raises exceptions for errors.

        :param response: The response object from the requests library
        :return: Parsed JSON response if successful
        :raises Exception: If the response status code indicates an error
        """
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
