def add_key_value(d, key, value):
    """Add a key-value pair to the dictionary."""
    d[key] = value

def remove_key(d, key):
    """Remove a key-value pair from the dictionary using the key."""
    d.pop(key, None)

def merge_dicts(d1, d2):
    """Merge two dictionaries."""
    return {**d1, **d2}
