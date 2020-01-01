
class BinarySearchTree:

    def __init__(self):
        self.root = None
        # build method missing

    def search(k):
        node = self.root
        while node and node.key != k:
            if k < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def minimum(node=None):
        node = self.root if node is None else node
        while node.left:
            node = node.left
        return node

    def maximum(node=None):
        node = self.root if node is None else node
        while node.right:
            node = node.right
        return node

    def successor(node):
        if node.right:
            return self.minimum(node.right)
        while node.parent and node is node.parent.right:
             node = node.parent
        return node.parent
            
    def predessor(node):
        if node.left:
            return self.maximum(node.left)
        while node.parent and node is node.parent.left:
            node = node.parent
        return node.parent

    def insert(node):
        y, x = None, self.root
        while x:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.p = y
        if y is None:
            self.root = z
        elif node.key < y.key:
            y.left = z
        else:
            y.right = z
