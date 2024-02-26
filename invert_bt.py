'Given the root of a binary tree, invert the tree, and return its root.'

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
    
# Helper to print the tree
def print_tree(root):
    queue = [(root, 'Root', 0)]
    while len(queue) != 0:
        node, direction, level = queue.pop(0)
        print(f'Level {level}: {direction} Node {node.val}')
        if node.left is not None:
            queue.append((node.left, 'left', level + 1))
        if node.right is not None:
            queue.append((node.right, 'right', level + 1))

def invert_bt(root):
    if root is None:
        return root
    # Level order traversal with queue
    queue = [root]
    while len(queue) != 0:
        node = queue.pop(0)
        # Save left and right children
        left_child = node.left
        right_child = node.right
        # Swap children
        node.right = left_child
        node.left = right_child
        # Add children to queue
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return root

# TESTS
        
node1 = Node(4)
node2 = Node(2)
node3 = Node(7)
node4 = Node(1)
node5 = Node(3)
node6 = Node(6)
node7 = Node(9)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# print_tree(node1)
print_tree(invert_bt(node1))

# print(node1)
