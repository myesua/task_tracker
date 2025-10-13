#!/bin/bash

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run bandit security scans
echo "Running bandit security scans..."
bandit -r examples/ -f json -o bandit_results.json
echo "Bandit results saved to bandit_results.json"

# Run flake8 style checks
echo "Running flake8 style checks..."
flake8 examples/ --output-file=flake8_results.txt
echo "Flake8 results saved to flake8_results.txt"

# Run unit tests
echo "Running unit tests..."
python test_security_patterns.py

# Display results
echo ""
echo "=== Security Scan Results ==="
if [ -f bandit_results.json ]; then
    cat bandit_results.json
else
    echo "No bandit results file found"
fi

echo ""
echo "=== Style Check Results ==="
if [ -f flake8_results.txt ]; then
    cat flake8_results.txt
else
    echo "No flake8 results file found"
fi

echo ""
echo "=== Test Results ==="
python test_security_patterns.py

echo ""
echo "Scan completed!"