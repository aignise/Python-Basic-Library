def write_to_file(filename, content):
    """
    Write content to a file. If the file already exists, it will be overwritten.

    Args:
    - filename (str): The name of the file to write to.
    - content (str): The content to write to the file.
    """
    with open(filename, 'w') as file:
        file.write(content)

def append_to_file(filename, content):
    """
    Append content to a file.

    Args:
    - filename (str): The name of the file to append to.
    - content (str): The content to append to the file.
    """
    with open(filename, 'a') as file:
        file.write(content)
