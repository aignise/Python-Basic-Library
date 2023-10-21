# Data Structures Module

The `data_structures` module provides implementations of foundational data structures, including stacks, queues, trees, and graphs. Each data structure is designed to be intuitive and modular, making it easy to integrate and expand upon.

## Files & Descriptions

### 1. `stacks.py`
- Implementation of the stack data structure.
    - `push(item)`: Push an item onto the stack.
    - `pop()`: Pop an item off the stack.
    - `peek()`: Peek at the top item without removing it.
    - `is_empty()`: Check if the stack is empty.
    - `size()`: Return the number of items in the stack.

### 2. `queues.py`
- Implementation of the queue data structure.
    - `enqueue(item)`: Add an item to the end of the queue.
    - `dequeue()`: Remove an item from the front of the queue.
    - `peek()`: Look at the front item without removing it.
    - `is_empty()`: Check if the queue is empty.
    - `size()`: Return the number of items in the queue.

### 3. `trees.py`
- Basic binary tree implementation with traversal methods.
    - `inorder_traversal()`: Inorder traversal of the tree.

### 4. `graphs.py`
- Basic undirected graph implementation using an adjacency list.
    - `add_vertex(vertex)`: Add a vertex to the graph.
    - `add_edge(vertex1, vertex2)`: Add an edge between two vertices.
    - `show_edges()`: Display the edges of the graph.

## Usage

To use any data structure from this module, simply import the desired class and instantiate it. For example:
```python
from data_structures.stacks import Stack
s = Stack()
s.push(5)
print(s.peek())  # Outputs: 5
