// scripts/api.js

const API_BASE_URL = '/api';

async function fetchResources() {
    const response = await fetch(`${API_BASE_URL}/resources`);
    if (!response.ok) throw new Error('Failed to fetch resources');
    return await response.json();
}

async function submitTransaction(transaction) {
    const response = await fetch(`${API_BASE_URL}/transactions/new`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(transaction)
    });
    if (!response.ok) throw new Error('Transaction failed');
    return await response.json();
}

export { fetchResources, submitTransaction };
