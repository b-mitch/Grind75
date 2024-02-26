'Given a binary tree, determine if it is height-balanced.'

'A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.'

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Quick recursive helper to traverse left and right subtrees and return max depth
def get_levels(node, level):
    if node is None:
        return level
    
    return max(get_levels(node.left, level + 1), get_levels(node.right, level + 1))

# Helper function to compare left and right subtree depths
def is_balanced_subtree(root):
    levels_left = get_levels(root.left, 0) if root.left else 0
    levels_right = get_levels(root.right, 0) if root.right else 0
    diff = levels_left - levels_right
    return (diff >= -1 and diff <= 1)

def is_balanced(root):
    # Empty trees are balanced
    if root is None:
        return True
    # Use a stack to DF traverse the tree
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        # Check if current subtree is balanced
        if not is_balanced_subtree(node):
            return False
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return True
    

# TESTS
        
node1 = Node(3)
node2 = Node(9)
node3 = Node(20)
node4 = Node(15)
node5 = Node(7)
node6 = Node(5)
node7 = Node(12)

node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5
node4.left = node6
node5.right = node7


print(is_balanced(node1))