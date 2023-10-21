import os

def create_directory(path):
    """
    Creates a new directory at the specified path.

    Args:
    - path (str): Path where the new directory should be created.
    """
    os.makedirs(path, exist_ok=True)

def delete_directory(path):
    """
    Deletes the directory at the specified path.

    Args:
    - path (str): Path of the directory to delete.
    """
    if os.path.exists(path) and os.path.isdir(path):
        os.rmdir(path)

def current_directory():
    """
    Returns the current working directory.
    
    Returns:
    - str: Path of the current working directory.
    """
    return os.getcwd()

def change_directory(path):
    """
    Changes the current working directory to the specified path.

    Args:
    - path (str): The directory path to change to.
    """
    os.chdir(path)

def list_files(path='.'):
    """
    Lists files and directories in the specified path.

    Args:
    - path (str, optional): The directory path to list. Defaults to current directory.

    Returns:
    - list: List of files and directories in the specified path.
    """
    return os.listdir(path)
