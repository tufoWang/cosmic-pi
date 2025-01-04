# examples/demo_transaction.py

import requests

def create_transaction(sender, recipient, amount):
    """Creates a new transaction and submits it to the blockchain."""
    url = 'http://localhost:5000/api/transactions/new'  # Adjust the URL as needed
    transaction_data = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    response = requests.post(url, json=transaction_data)
    
    if response.status_code == 201:
        print("Transaction submitted successfully:")
        print(response.json())
    else:
        print("Failed to submit transaction:")
        print(response.status_code, response.text)

if __name__ == "__main__":
    # Example usage
    create_transaction(sender="Alice", recipient="Bob", amount=50)
