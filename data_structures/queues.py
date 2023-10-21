class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove an item from the front of the queue."""
        if not self.is_empty():
            return self.queue.pop(0)

    def peek(self):
        """Look at the front item without removing it."""
        if not self.is_empty():
            return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)
