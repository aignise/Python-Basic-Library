# Lists Module

The `lists` module provides a collection of functions to facilitate operations and manipulations on Python lists. Each function is designed to handle a specific operation, making the module modular and user-friendly.

## Files & Descriptions

### 1. `manipulation.py`
- Basic and advanced list manipulations.
    - `add_element(lst, element, index=None)`: Add an element to the list. If an index is provided, insert at that index.
    - `remove_element(lst, element)`: Remove an element from the list.
    - `reverse_list(lst)`: Reverse the list in-place.
    - `sort_list(lst, reverse=False)`: Sort the list. If `reverse` is True, sort in descending order.

### 2. `traversal.py`
- Traversal operations on lists.
    - `traverse_list(lst)`: Print each element of the list.

### 3. `search.py`
- Search operations within lists.
    - `find_element(lst, element)`: Return the index of an element in the list or -1 if not found.
    - `count_element(lst, element)`: Count occurrences of an element in the list.

### 4. `conversion.py`
- Conversions related to lists.
    - `list_to_string(lst, delimiter=",")`: Convert a list to a string, using the specified delimiter.
    - `string_to_list(s, delimiter=",")`: Convert a string to a list, splitting by the delimiter.

## Usage

To use any function from the `lists` module, simply import the desired function and call it in your code. For example:
```python
from lists.manipulation import add_element
lst = [1, 2, 3]
add_element(lst, 4)
print(lst)  # Outputs: [1, 2, 3, 4]
