# scripts/monitor.py

import requests
import time

def check_service(url):
    """Check if a service is up and running."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Service {url} is up.")
        else:
            print(f"Service {url} returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Service {url} is down. Error: {e}")

def monitor():
    """Monitor application services."""
    services = [
        'http://localhost:5000/api',  # Example API endpoint
        'https://api.paymentservice.com',
        'https://api.spaceresource.com',
    ]

    while True:
        for service in services:
            check_service(service)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    monitor()
