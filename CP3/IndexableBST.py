# Mostly from CLRS 3rd Ed
# For indexing to work correctly, keys MUST be unique
# Everything has been tested, except index_node()

class Node:
    
    def __init__(self, key, left=None, right=None, data=None):
        self.key, self.left, self.right = key, left, right
        self.parent, self.data, self.size = None, data, 1
        
    # Methods to automatically update parent/size
    def add_right(self, key=None, node=None):
        if node:
            self.right = node
            self._propagate(self)
        elif key is not None:
            self.right = Node(key)
            self._propagate(self)

    def add_left(self, key=None, node=None):
        if node:
            self.left = node
            self._propagate(self)
        elif key is not None:
            self.left = Node(key)
            self._propagate(self)

    # Overlaps with BST methods, not good?
    def _propagate(self, node):
        while node:
            node.size = self._getSize(node.left) + self._getSize(node.right) + 1
            node = node.parent

    def _getSize(self, node):
        return node.size if node else 0


class BinarySearchTree:

    def __init__(self, initializer=None, key=lambda x: x):
        
        def build(left, right): 
            ret_node, count = None, 0
            if left == right:
                ret_node, count =  Node(contents[left]), 1
            elif left < right:
                mid = (left + right) // 2
                ret_node = Node(contents[mid])
                ret_node.left, leftCount = build(left, mid - 1)
                ret_node.right, rightCount = build(mid + 1, right) 
                ret_node.size = count = 1 + leftCount + rightCount
                if ret_node.left:
                    ret_node.left.parent = ret_node
                if ret_node.right:
                    ret_node.right.parent = ret_node
            return ret_node, count
            
        # O(nlogn) to build BST using this method
        self.root = None
        if initializer:
            contents = sorted(initializer, key=key)
            self.root, _ = build(0, len(contents) - 1)

    def search(self, k):
        node = self.root
        while node and node.key != k:
            if k < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def minimum(self, node=None):
        node = self.root if node is None else node
        while node.left:
            node = node.left
        return node

    def maximum(self, node=None):
        node = self.root if node is None else node
        while node.right:
            node = node.right
        return node

    def successor(self, node):
        if node.right:
            return self.minimum(node.right)
        while node.parent and node is node.parent.right:
             node = node.parent
        return node.parent
            
    def predessor(self, node):
        if node.left:
            return self.maximum(node.left)
        while node.parent and node is node.parent.left:
            node = node.parent
        return node.parent

    # node must have a unique key
    def insert(self, node):
        y, x = None, self.root
        while x:
            y = x
            x.size += node.size     #
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        self._propagate(u.parent)
        if v:
            v.parent, u.parent = u.parent, None

    # Propagate size changes up the BST
    def _propagate(self, node):
        while node:
            node.size = self._getSize(node.left) + self._getSize(node.right) + 1   
            node = node.parent

    def delete(self, key):
        node = self.search(key)
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
            self._propagate(y)

    # Gets (i + 1)th node from in order traversal 
    def __getitem__(self, i):
        i, node = i + 1, self.root
        while node:
            left_size = self._getSize(node.left)
            if left_size + 1 < i:
                i -= left_size + 1
                node = node.right
            elif left_size == i - 1:
                return node
            else:
                node = node.left
        return node

    def _getSize(self, node):
        return node.size if node else 0

    def index(self, key):
        tree, count = self.root, 0
        while tree and tree.key != key:
            if key < tree.key:
                tree = tree.left
            else:
                count += self._getSize(tree.left) + 1
                tree = tree.right
        # Will give nonsense answer if key not found in this tree
        return self._getSize(tree.left) + count 

    # Get index by node, won't be any good if not part of BST unlike 
    # index()
    # Not tested 
    def index_node(self, node):
        left_size, count = self._getSize(node.left), 0
        while node.parent and node is node.parent.right: 
            node = node.parent
            count += self._getSize(node)
        return left_size + count
