'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_depth(root):
    if root is None:
        return 0
    depth = 1
    # BFT with queue
    queue = []
    queue.append((root, depth))
    while len(queue):
        node, level = queue.pop(0)
        # Update depth based on current level
        depth = level
        # Add children and their level to queue
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return depth

# TESTS
        
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

print(max_depth(node1))
# >> 3
