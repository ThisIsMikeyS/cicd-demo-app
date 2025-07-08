"""
calculator.py

A simple arithmetic module for demonstration purposes in a CI/CD pipeline.

This module provides four basic math operations:
- add(a, b): return the sum of two numbers
- subtract(a, b): return the difference of two numbers
- multiply(a, b): return the product of two numbers
- divide(a, b): return the quotient of two numbers, with division-by-zero handling

This code is designed to be used with accompanying unit tests in a GitHub Actions
CI workflow. It is compatible with Python 3.10+ and works on Windows, Linux, and macOS.

Author: Michael Saunders
License: MIT
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
