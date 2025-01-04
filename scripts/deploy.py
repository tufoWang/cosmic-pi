# scripts/deploy.py

import os
import subprocess

def deploy():
    """Deploy the application."""
    print("Starting deployment...")

    # Pull the latest code from the repository
    subprocess.run(["git", "pull"], check=True)

    # Install dependencies
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

    # Run database migrations
    subprocess.run(["python", "migrate.py"], check=True)

    # Start the application (this can vary based on your setup)
    subprocess.run(["gunicorn", "src.api.app:app", "-b", "0.0.0.0:5000"], check=True)

    print("Deployment completed successfully.")

if __name__ == "__main__":
    deploy()
