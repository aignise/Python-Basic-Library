class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)

    def pop(self):
        """Pop an item off the stack."""
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        """Peek at the top item without removing it."""
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)
