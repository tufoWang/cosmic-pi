import requests

class Oracle:
    def __init__(self, oracle_url):
        self.oracle_url = oracle_url

    def get_price(self, asset):
        response = requests.get(f"{self.oracle_url}/price/{asset}")
        if response.status_code == 200:
            return response.json()['price']
        else:
            raise Exception("Failed to fetch price data from oracle")

    def get_weather(self, location):
        response = requests.get(f"{self.oracle_url}/weather/{location}")
        if response.status_code == 200:
            return response.json()['weather']
        else:
            raise Exception("Failed to fetch weather data from oracle")
