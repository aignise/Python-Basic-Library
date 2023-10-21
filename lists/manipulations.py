def add_element(lst, element, index=None):
    """Add an element to the list. If index is provided, insert at that index."""
    if index is None:
        lst.append(element)
    else:
        lst.insert(index, element)

def remove_element(lst, element):
    """Remove an element from the list."""
    lst.remove(element)

def reverse_list(lst):
    """Reverse the list in-place."""
    lst.reverse()

def sort_list(lst, reverse=False):
    """Sort the list. If reverse is True, sort in descending order."""
    lst.sort(reverse=reverse)
