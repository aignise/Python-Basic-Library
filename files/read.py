import os

def read_entire_file(filename):
    """
    Read and return the entire content of a file.

    Args:
    - filename (str): The name of the file to read.

    Returns:
    - str: The content of the file.
    """
    with open(filename, 'r') as file:
        return file.read()

def read_file_by_lines(filename):
    """
    Read and return the content of a file line by line.

    Args:
    - filename (str): The name of the file to read.

    Returns:
    - list: A list where each item is a line from the file.
    """
    with open(filename, 'r') as file:
        return file.readlines()

def read_specific_line(filename, line_number):
    """
    Read and return a specific line from a file.

    Args:
    - filename (str): The name of the file to read.
    - line_number (int): The line number to read.

    Returns:
    - str: The content of the specified line.
    """
    with open(filename, 'r') as file:
        for current_line_number, line in enumerate(file, start=1):
            if current_line_number == line_number:
                return line.strip()

def get_file_size(path):
    """
    Retrieves the size of a file.

    Args:
    - path (str): Path to the file.

    Returns:
    - int: Size of the file in bytes.
    """
    return os.path.getsize(path)

def get_file_modified_time(path):
    """
    Retrieves the last modified time of a file.

    Args:
    - path (str): Path to the file.

    Returns:
    - float: Time of the last modification, measured in seconds since the epoch.
    """
    return os.path.getmtime(path)

def check_permission(path, mode):
    """
    Checks for a specific permission on a file or directory.

    Args:
    - path (str): Path to the file or directory.
    - mode (str): Permission mode to check ('r' for read, 'w' for write, 'x' for execute).

    Returns:
    - bool: True if permission exists, False otherwise.
    """
    if mode == 'r':
        return os.access(path, os.R_OK)
    elif mode == 'w':
        return os.access(path, os.W_OK)
    elif mode == 'x':
        return os.access(path, os.X_OK)

def create_symbolic_link(source, destination):
    """
    Creates a symbolic link pointing to the source file at the destination path.

    Args:
    - source (str): Path to the source file.
    - destination (str): Path where the symbolic link should be created.
    """
    os.symlink(source, destination)