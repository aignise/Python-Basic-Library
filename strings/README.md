# Strings Module

The `strings` module encompasses a wide range of operations and manipulations related to Python strings. It offers a collection of functions, each focusing on a specific operation, ensuring modularity and ease of use.

## Files & Descriptions

### 1. `manipulation.py`
- Basic and advanced string manipulations.
    - `concatenate(str1, str2)`: Concatenate two strings.
    - `reverse_string(s)`: Reverse a string.
    - `capitalize_first(s)`: Capitalize the first letter of a string.
    - `capitalize_each_word(s)`: Capitalize the first letter of each word in a string.
    - `snake_to_camel(s)`: Convert a snake_case string to camelCase.
    - `camel_to_snake(s)`: Convert a camelCase string to snake_case.
    - `capitalize_sentence(s)`: Capitalize only the first letter of the first word in a sentence.

### 2. `formatting.py`
- Formatting strings.
    - `format_with_fstring(name, age)`: Format string using f-string.
    - `format_with_format(name, age)`: Format string using the `str.format` method.

### 3. `search.py`
- Search operations within strings.
    - `find_substring(s, substring)`: Find a substring in a string.
    - `starts_with_prefix(s, prefix)`: Check if a string starts with a given prefix.
    - `ends_with_suffix(s, suffix)`: Check if a string ends with a given suffix.

### 4. `conversion.py`
- Conversions related to strings.
    - `string_to_int(s)`: Convert a string to an integer.
    - `string_to_float(s)`: Convert a string to a float.

## Usage

To use any function from the `strings` module, simply import the desired function and call it in your code. For example:
```python
from strings.manipulation import concatenate
result = concatenate("Hello", " World")
print(result)  # Outputs: Hello World
