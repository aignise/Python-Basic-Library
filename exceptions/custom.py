class InvalidAgeError(Exception):
    """Custom exception for invalid age values."""
    pass

def validate_age(age):
    """
    Validates if a given age is within a reasonable range (0-120). If not, it raises a custom exception.

    Args:
    - age (int): Age value to validate.

    Raises:
    - InvalidAgeError: If age is not within the 0-120 range.
    """
    if age < 0 or age > 120:
        raise InvalidAgeError("Age should be between 0 and 120!")
