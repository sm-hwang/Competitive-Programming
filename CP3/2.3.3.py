
class BsTNode:
    
    def __init__(self, key, left=None, right=None, parent=None):
        self.key, self.left, self.right = key, left, right
        self.parent = parent # if needed

# Usual inorder traversal of BST gives keys in ascending, but visiting the right subtree before left subtree gives key
# in descending order. 
def leaves_in_descending(tree):
    if tree:
        leaves_in_descending(tree.right)
        if tree.right is None and tree.left is None: # If node is a leaf
            print(tree.key)
        leaves_in_descending(tree.left)
       
# in_range1 traverses BST inorder (therefore ascending order) and prints the key if its in the range
def in_range1(tree, lower, upper):
    if tree:
        in_range1(tree.left, lower, upper)
        if lower <= tree.key <= upper:
            print(tree.key)
        in_range1(tree.right, lower, upper)
        
# in_range2 does the same thing as in_range1, but is more selective on what subtrees to visit based on key
# if the current subtree contains a key less than lower, its left subtree won't contain a key in the range 
def in_range2(tree, lower, upper):
    if tree:
        if lower <= tree.key:
            in_range2(tree.left, lower, upper)
        if lower <= tree.key <= upper:
            print(tree.key)
        if tree.key <= upper:
            in_range2(tree.right, lower, upper)
       
