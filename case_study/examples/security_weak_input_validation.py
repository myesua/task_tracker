"""
SECURITY ANTI-PATTERN: Weak Input Validation
Risk: SQL Injection, Command Injection, Data Corruption
Detection: Bandit B105, B106
Severity: High

This example shows weak input validation where user input is directly used
in database queries and shell commands without proper sanitization.
"""

import sqlite3
import subprocess

def search_database(user_input):
    """
    VULNERABLE: Direct string formatting in SQL query
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    results = cursor.fetchall()
    
    conn.close()
    return results

def search_database_fixed(user_input):
    """
    FIXED: Parameterized queries with input validation
    """
    # Validate input length and content
    if len(user_input) > 100:
        raise ValueError("Input too long")
    
    if not user_input.isprintable():
        raise ValueError("Invalid characters in input")
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Safe parameterized query
    query = "SELECT * FROM users WHERE name = ?"
    cursor.execute(query, (user_input,))
    results = cursor.fetchall()
    
    conn.close()
    return results

def run_command(user_input):
    """
    VULNERABLE: Shell command with user input
    """
    # Command injection vulnerability
    command = f"ls -la {user_input}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def run_command_fixed(user_input):
    """
    FIXED: Command with proper input validation and subprocess without shell=True
    """
    # Validate input
    if not user_input.replace('/', '').replace('-', '').replace('_', '').isalnum():
        raise ValueError("Invalid characters in path")
    
    # Safe subprocess usage without shell=True
    result = subprocess.run(['ls', '-la', user_input], capture_output=True, text=True)
    return result.stdout

# Example usage
if __name__ == "__main__":
    user_input = "test"
    print(search_database(user_input))
    print(search_database_fixed(user_input))
    print(run_command(user_input))
    print(run_command_fixed(user_input))