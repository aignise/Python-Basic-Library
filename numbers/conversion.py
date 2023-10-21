
def int_to_float(n):
    """Convert an integer to a float."""
    return float(n)

def float_to_int(f):
    """Convert a float to an integer."""
    return int(f)

def number_to_string(num):
    """Convert a number (int or float) to a string."""
    return str(num)

def string_to_number(s):
    """Convert a string to a number (int or float, based on its content)."""
    try:
        return int(s)
    except ValueError:
        return float(s)
