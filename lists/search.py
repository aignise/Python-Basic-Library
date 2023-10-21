def find_element(lst, element):
    """Return the index of an element in the list or -1 if not found."""
    return lst.index(element) if element in lst else -1

def count_element(lst, element):
    """Count occurrences of an element in the list."""
    return lst.count(element)
