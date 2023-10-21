def handle_exception(exception_type, default_return):
    """
    Decorator function to handle specific exceptions for a function and return a default value.

    Args:
    - exception_type (Exception): The type of exception to handle.
    - default_return (any): The default value to return when the exception is caught.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type:
                return default_return
        return wrapper
    return decorator
