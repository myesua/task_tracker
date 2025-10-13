"""
SECURITY ANTI-PATTERN: Hardcoded Secrets
Risk: Credential Exposure, Unauthorized Access
Detection: Bandit B105, B602
Severity: Critical

This example shows hardcoded API keys, passwords, and sensitive data
in source code, which should never be committed to version control.
"""

import os

# VULNERABLE: Hardcoded secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "super_secret_password"
JWT_SECRET = "my_very_secret_jwt_key"

def make_api_request():
    """
    VULNERABLE: Uses hardcoded API key
    """
    import requests
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.get("https://api.example.com/data", headers=headers)
    return response.json()

def make_api_request_fixed():
    """
    FIXED: Uses environment variables for secrets
    """
    import requests
    
    # Get secrets from environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    response = requests.get("https://api.example.com/data", headers=headers)
    return response.json()

def connect_to_database():
    """
    VULNERABLE: Hardcoded database password
    """
    import psycopg2
    
    conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="admin",
        password=DATABASE_PASSWORD  # Hardcoded password
    )
    return conn

def connect_to_database_fixed():
    """
    FIXED: Uses environment variables for database credentials
    """
    import psycopg2
    
    db_config = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'database': os.getenv('DB_NAME', 'mydb'),
        'user': os.getenv('DB_USER', 'admin'),
        'password': os.getenv('DB_PASSWORD')
    }
    
    if not db_config['password']:
        raise ValueError("DB_PASSWORD environment variable not set")
    
    conn = psycopg2.connect(**db_config)
    return conn

# Example usage
if __name__ == "__main__":
    print(make_api_request())
    print(make_api_request_fixed())
    print(connect_to_database())
    print(connect_to_database_fixed())