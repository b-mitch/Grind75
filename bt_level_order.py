'Given the root of a binary tree, return the level order traversal of its nodes values. (i.e., from left to right, level by level).'

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(root):
    # Account for empty Node
    if not root:
        return []
    # Track all nodes, current level nodes and current level
    nodes, level_nodes, current_level = [], [], 1
    # Create queue for level order traversal, using tuples to track node and level
    queue = [(root, current_level)]
    while len(queue):
        node, node_level = queue.pop(0)
        # If current node level differs from current level, we're on a new level
        if node_level != current_level:
            # Add previous level's nodes and reset the array and current level
            nodes.append(level_nodes)
            level_nodes = []
            current_level = node_level
        # Add current node to current level's nodes array
        level_nodes.append(node.val)
        # Add children nodes to queue
        if node.left:
            queue.append((node.left, node_level + 1))
        if node.right:
            queue.append((node.right, node_level + 1))
    # Add last level's nodes
    nodes.append(level_nodes)
    return nodes

# TESTS
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

print(level_order(node1))
# >>[[1],[2,3],[4,5,6,7]]