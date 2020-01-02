# Mostly from CLRS 3rd Ed
# Might change to make methods take "key" instead of "node"
# For indexing to work correctly, keys MUST be unique
# index() has been tested

class Node:
    
    def __init__(self, key, left=None, right=None, data=None):
        self.key, self.left, self.right = key, left, right
        self.parent, self.data, self.size = None, data, 1


class BinarySearchTree:

    def __init__(self, initializer, key=lambda x: x):
        
        def build(left, right): 
            ret_node, count = None, 0
            if left == right:
                ret_node, count =  Node(key(contents[left])), 1
            elif left < right:
                mid = (left + right) // 2
                ret_node = Node(key(contents[mid]))
                ret_node.left, leftCount = build(left, mid - 1)
                ret_node.right, rightCount = build(mid + 1, right) 
                ret_node.size = count = 1 + leftCount + rightCount
                if ret_node.left:
                    ret_node.left.parent = ret_node
                if ret_node.right:
                    ret_node.right.parent = ret_node
            return ret_node, count
        
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
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left, y.size = node, y.size + node.size
        else:
            y.right, y.size = node, y.size + node.size

    # Changed from CLRS to remove u's reference to parent 
    # To make size calculation with delete correct
    def transplant(self, u, v):
        u_size, v_size = self._getSize(u), self._getSize(v)
        if not u.parent:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
            u.parent.size += v_size - u_size
        else:
            u.parent.left = v
            u.parent.size += v_size - u_size
        if v:
            if v.parent:
                v.parent.size -= v_size
            v.parent, u.parent = u.parent, None

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
                y.size += self._getSize(y.right)
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.size += self._getSize(y.left)
            
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
    
    def index_node(self, node):
        left_size, count = self._getSize(node.left), 0
        while node.parent and node is node.parent.right: 
            node = node.parent
            count += self._getSize(node)
        return left_size + count
