def list_to_string(lst, delimiter=","):
    """Convert a list to a string, using the delimiter."""
    return delimiter.join(map(str, lst))

def string_to_list(s, delimiter=","):
    """Convert a string to a list, splitting by the delimiter."""
    return s.split(delimiter)
