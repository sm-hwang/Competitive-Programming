# Mostly from CLRS 3rd Ed
# Might change to make methods take "key" instead of "node"

class Node:
    
    def __init__(self, key, left=None, right=None, data=None):
        self.key, self.left, self.right = key, left, right
        self.parent, self.data, self.size = None, data, 1


class BinarySearchTree:

    def __init__(self, initializer, key=lambda x: x):
        
        def build(left, right): 
            if left == right:
                ret_node, size = Node(key(contents[left])), 1
            elif left < right:
                mid = (left + right) // 2
                ret_node = Node(key(contents[mid]))
                ret_node.left, left_size = build(left, mid - 1)
                ret_node.right, right_size = build(mid + 1, right)
                ret_node.size = size = 1 + left_count + right_count
            return ret_node, size
        
        # O(nlogn) build time for a minimum height Binary Search Tree
        contents = sorted(initializer, key=key)
        self.root, _ = build(0, len(contents) - 1)

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


    def delete(self, node):
        if not node.left:
            self.transplant(node, node.right) 
        elif not node.right:
            self.transplant(node, node.left) 
        else:
            y = self.minimum(node.right)
            if y.parent is not node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            
    # Get (i + 1)th element of inorder traversal
    # From Elements of Programming Interviews (Python)
    def __getitem__(self, i):
        i, node = i + 1, self.root
        while node:
            left_size = self._getSize(node.left)
            if left_size + 1 < i:
                i -= left_size + 1
                node = node.right
            elif left_size == i - 1:
                break
            else:
                node = node.left
        return node
    
    def _getSize(self, node):
        return node.size if node else 0

    # Should take as input "key" instead of node?
    def index(self, node):
        tree, count = self.root, 0
        while tree and tree.key != node.key:
            if node.key < tree.key:
                tree = tree.left
            else:
                count += self._getSize(tree.left) + 1
                tree = tree.right
        # Will give nonsense answer if node.key not found in this tree
        return self._getSize(tree.left) + count
