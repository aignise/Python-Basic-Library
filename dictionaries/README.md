# Dictionaries Module

The `dictionaries` module provides a suite of functions designed to facilitate various operations and manipulations on Python dictionaries. Whether you're looking to manipulate, traverse, search, or convert dictionaries, this module has got you covered.

## Files & Descriptions

### 1. `manipulation.py`
- Fundamental dictionary manipulation functions.
    - `add_key_value(d, key, value)`: Add a key-value pair to the dictionary.
    - `remove_key(d, key)`: Remove a key-value pair using the key.
    - `merge_dicts(d1, d2)`: Merge two dictionaries into one.

### 2. `traversal.py`
- Traversal operations for dictionaries.
    - `get_keys(d)`: Retrieve all keys from the dictionary.
    - `get_values(d)`: Retrieve all values from the dictionary.
    - `get_items(d)`: Retrieve all key-value pairs (items) from the dictionary.

### 3. `search.py`
- Searching within dictionaries.
    - `has_key(d, key)`: Check if a specific key exists in the dictionary.
    - `has_value(d, value)`: Check if a specific value is present in the dictionary.

### 4. `conversion.py`
- Convert dictionaries to and from other data types.
    - `dict_to_list_of_tuples(d)`: Convert a dictionary to a list of its key-value pairs (as tuples).
    - `list_of_tuples_to_dict(lst)`: Convert a list of tuples into a dictionary.

## Usage

To utilize any function from the `dictionaries` module, simply import the required function and use it in your code. For instance:
```python
from dictionaries.manipulation import add_key_value
d = {"name": "John"}
add_key_value(d, "age", 30)
print(d)  # Outputs: {"name": "John", "age": 30}
