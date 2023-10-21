import os

def file_exists(filename):
    """
    Check if a file exists.

    Args:
    - filename (str): The name of the file to check.

    Returns:
    - bool: True if the file exists, False otherwise.
    """
    return os.path.exists(filename)

def delete_file(filename):
    """
    Delete a file.

    Args:
    - filename (str): The name of the file to delete.
    """
    if file_exists(filename):
        os.remove(filename)

def rename_file(old_name, new_name):
    """
    Rename a file.

    Args:
    - old_name (str): The current name of the file.
    - new_name (str): The new name for the file.
    """
    if file_exists(old_name):
        os.rename(old_name, new_name)
