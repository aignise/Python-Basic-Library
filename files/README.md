# File I/O and Directory Management Module

The `files_io` module encompasses a wide range of functionalities tailored for file reading/writing, directory management, and advanced file system operations.

## 1. Reading and Writing Files

### `read.py`

Offers methods to read content from files.

- **`read_entire_file(filename)`**:
    - Read and return the entire content of a file.
  
- **`read_file_by_lines(filename)`**:
    - Read and return the content of a file line by line.
  
- **`read_specific_line(filename, line_number)`**:
    - Read and return a specific line from a file.
  
- **`check_permission(path, mode)`**:
    - Checks for a specific permission on a file or directory. Modes include 'r' (read), 'w' (write), and 'x' (execute).

### File Properties

- **`get_file_size(path)`**:
    - Retrieves the size of a file in bytes.
  
- **`get_file_modified_time(path)`**:
    - Retrieves the last modified time of a file.

### `write.py`

Provides methods to write content to files.

- **`write_to_file(filename, content)`**:
    - Write content to a file. If the file already exists, it will be overwritten.
  
- **`append_to_file(filename, content)`**:
    - Append content to a file.

## 2. Directory Management (`directory_management.py`)

This script offers a range of functions to manage directories, navigate the file system, inspect file properties, and perform advanced operations.

### Navigation

- **`current_directory()`**:
    - Returns the current working directory.
  
- **`change_directory(path)`**:
    - Changes the current working directory to the specified path.
  
- **`list_files(path='.')`**:
    - Lists files and directories in the specified path. Defaults to the current directory.

### Directory Operations

- **`create_directory(path)`**:
    - Creates a new directory at the specified path.
  
- **`delete_directory(path)`**:
    - Deletes the directory at the specified path.


### Advanced Operations

- **`create_symbolic_link(source, destination)`**:
    - Creates a symbolic link pointing to the source file at the destination path.

## Usage

To harness the functionalities provided by this module, you'll first need to import the desired functions. Once imported, invoke them with the appropriate arguments. For example:

```python
from files_io.directory_management import list_files

# List all files and directories in the current working directory
print(list_files())
