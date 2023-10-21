class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def inorder_traversal(self, start, traversal=""):
        """Inorder traversal: Left -> Root -> Right"""
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.val) + ' ')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    # You can also implement preorder and postorder traversals.
