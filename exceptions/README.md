# Exceptions Handling Module

The `exceptions` module provides a robust framework for handling, raising, and testing exceptions in Python. This module encompasses fundamental exception handling techniques, custom exception definitions, utility functions for generic exception handling, and unit tests to ensure reliability.

## 1. Basic Exception Handling (`basics.py`)

This script showcases foundational techniques to handle exceptions using `try`, `except`, `else`, and `finally` blocks.

- **`safe_divide(a, b)`**: 
    - Safely divides two numbers. If the denominator is zero, it returns a message instead of raising an exception.

- **`list_element_retrieval(lst, index)`**: 
    - Retrieves an element from a list based on the given index. If the index is out of range, it returns an error message.

## 2. Custom Exceptions (`custom.py`)

Dive into the realm of custom exceptions, allowing for granular error handling tailored to specific needs.

- **`InvalidAgeError`**: 
    - A custom exception for invalid age values.

- **`validate_age(age)`**: 
    - Validates if a given age is within a reasonable range (0-120). If not, it raises the `InvalidAgeError`.

## 3. Utility Functions (`utils.py`)

Utility functions and decorators that can aid in exception handling across various scenarios.

- **`handle_exception(exception_type, default_return)`**: 
    - A decorator to handle specific exceptions for a function and return a default value when the exception is caught.

## 4. Unit Testing

A dedicated suite of unit tests to ensure that both basic and custom exception handling mechanisms work as intended.

    - Tests for the basic exception handling functions in `basics.py`.

    - Tests for the custom exceptions and related functions in `custom.py`.

## Running the Tests

To execute the tests, navigate to the `exceptions` directory and run:


This will automatically discover and run all tests within the `testing` directory.

## Feedback & Contributions

For feedback, improvements, or contributions, please reach out. Your insights and enhancements are invaluable in refining and expanding this module for various applications.


