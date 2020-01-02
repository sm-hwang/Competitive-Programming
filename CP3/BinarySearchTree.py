# Mostly from CLRS 3rd Ed
# Might change to make methods take "key" instead of "node"

class Node:
    
    def __init__(self, key, left=None, right=None, data=None):
        self.key, self.left, self.right = key, left, right
        self.parent, self.data = None, data

        
class BinarySearchTree:

    def __init__(self, initializer, key=lambda x: x):
        
        def build(left, right): 
            if left == right:
                ret_node= Node(key(contents[left]))
            elif left < right:
                mid = (left + right) // 2
                ret_node = Node(key(contents[mid]))
                ret_node.left = build(left, mid - 1)
                ret_node.right = build(mid + 1, right)
            return ret_node
        
        # O(nlogn) build time for a minimum height Binary Search Tree
        contents = sorted(initializer, key=key)
        self.root = build(0, len(contents) - 1)

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
