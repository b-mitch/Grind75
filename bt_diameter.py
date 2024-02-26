'''Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.'''

class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bt_diameter_helper(root, d):
    # Base case - If root is None, return 0
    if root is None:
        return 0
    # Get the left and right subtree diameters
    left_d = bt_diameter_helper(root.left, d)
    right_d = bt_diameter_helper(root.right, d)
    # Calculate their sum and replace diameter if greater
    sum_d = left_d + right_d
    d[0] = sum_d if sum_d > d[0] else d[0]
    # Return larger subtree diameter plus one
    return max(left_d, right_d) + 1

def bt_diameter(root):
    # Initialize an array with your diameter so you can change as needed
    d = [0]
    # Use helper to traverse tree recursively and update diameter
    bt_diameter_helper(root, d)
    return d[0]

# TESTS

node1 = BTNode(1)
node2 = BTNode(2)
node3 = BTNode(3)
node4 = BTNode(4)
node5 = BTNode(5)
node6 = BTNode(6)
node7 = BTNode(7)
node8 = BTNode(8)
node9 = BTNode(9)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node6
node5.right = node7
node6.left = node8
node7.right = node9

print(bt_diameter(node1))
# >> 6