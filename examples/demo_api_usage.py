# examples/demo_api_usage.py

import requests

def get_chain():
    """Fetches the current blockchain data."""
    url = 'http://localhost:5000/api/chain'  # Adjust the URL as needed
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Current Blockchain:")
        print(response.json())
    else:
        print("Failed to fetch blockchain data:")
        print(response.status_code, response.text)

def get_resources():
    """Fetches available resources."""
    url = 'http://localhost:5000/api/resources'  # Adjust the URL as needed
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Available Resources:")
        print(response.json())
    else:
        print("Failed to fetch resources:")
        print(response.status_code, response.text)

if __name__ == "__main__":
    # Example usage
    get_chain()
    get_resources()
