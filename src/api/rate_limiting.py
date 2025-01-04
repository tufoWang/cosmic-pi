from flask import request, jsonify
import time
from collections import defaultdict

# Rate limiting configuration
RATE_LIMIT = 5  # Maximum requests per time window
TIME_WINDOW = 60  # Time window in seconds

# In-memory storage for tracking requests
request_counts = defaultdict(lambda: {'count': 0, 'start_time': time.time()})

def rate_limiting_middleware():
    """Middleware for dynamic rate limiting API requests."""
    ip = request.remote_addr
    current_time = time.time()

    # Reset count if the time window has passed
    if current_time - request_counts[ip]['start_time'] > TIME_WINDOW:
        request_counts[ip] = {'count': 1, 'start_time': current_time}
    else:
        request_counts[ip]['count'] += 1

    # Check if the rate limit has been exceeded
    if request_counts[ip]['count'] > RATE_LIMIT:
        return jsonify({'error': 'Rate limit exceeded. Try again later.'}), 429
