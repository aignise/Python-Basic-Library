def safe_divide(a, b):
    """
    Safely divides two numbers. If the denominator is zero, it returns a message instead of raising an exception.

    Args:
    - a (float): Numerator.
    - b (float): Denominator.

    Returns:
    - float or str: Result of division or an error message if division by zero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

def list_element_retrieval(lst, index):
    """
    Retrieves an element from a list based on the given index. If the index is out of range, it returns an error message.

    Args:
    - lst (list): The list from which to retrieve the element.
    - index (int): The index of the desired element.

    Returns:
    - any or str: The element at the specified index or an error message if index is out of range.
    """
    try:
        return lst[index]
    except IndexError:
        return "Index out of range!"
