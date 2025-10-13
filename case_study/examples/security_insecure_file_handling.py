"""
SECURITY ANTI-PATTERN: Insecure File Handling
Risk: Path Traversal, Information Disclosure
Detection: Bandit B108, B605
Severity: High

This example shows insecure file handling where user input is directly used
to construct file paths without validation, potentially allowing path traversal attacks.
"""

import os

def get_user_file(user_input):
    """
    VULNERABLE: Directly uses user input to construct file path
    """
    file_path = f"/app/data/{user_input}"
    with open(file_path, 'r') as f:
        return f.read()

def get_user_file_fixed(user_input):
    """
    FIXED: Validates and sanitizes user input
    """
    # Validate input contains only allowed characters
    if not user_input.isalnum() and '_' not in user_input:
        raise ValueError("Invalid filename")
    
    # Prevent path traversal
    if '..' in user_input or '/' in user_input:
        raise ValueError("Invalid filename")
    
    file_path = f"/app/data/{user_input}"
    with open(file_path, 'r') as f:
        return f.read()

# Example usage
if __name__ == "__main__":
    # This would be vulnerable to path traversal: ../../etc/passwd
    user_input = "safe_file.txt"
    print(get_user_file(user_input))
    print(get_user_file_fixed(user_input))