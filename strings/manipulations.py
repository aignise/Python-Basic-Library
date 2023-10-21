def concatenate(str1, str2):
    """Concatenate two strings."""
    return str1 + str2

def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def capitalize_first(s):
    """Capitalize the first letter of a string."""
    return s.capitalize()

def capitalize_each_word(s):
    """Capitalize the first letter of each word in a string."""
    return ' '.join(word.capitalize() for word in s.split())

def snake_to_camel(s):
    """Convert a snake_case string to camelCase."""
    words = s.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

def camel_to_snake(s):
    """Convert a camelCase string to snake_case."""
    result = [s[0].lower()]
    for char in s[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)
    return ''.join(result)

def capitalize_sentence(s):
    """Capitalize only the first letter of the first word in a sentence."""
    return s[0].capitalize() + s[1:] if s else ''
