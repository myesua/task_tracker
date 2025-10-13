# Code Review API Case Study

This directory contains educational examples of security and performance anti-patterns for testing code review APIs.

## Purpose

- **Security**: Demonstrate common security vulnerabilities that code review APIs should detect
- **Performance**: Show performance anti-patterns that automated reviewers should flag
- **Testing**: Provide ground truth for testing code review API accuracy

## Structure

- `anti_patterns.md` - Descriptions of common anti-patterns
- `examples/` - Code examples showing problematic patterns and their fixes
- `detection_tests/` - Unit tests to verify linters correctly flag patterns

## Usage

1. Run detection tests: `python -m pytest detection_tests/`
2. Run linters: `bandit -r examples/ && flake8 examples/`
3. Use examples as ground truth for training code review APIs

## Safety

All examples are educational and safe. No exploit code or instructions to weaponize vulnerabilities are included.
