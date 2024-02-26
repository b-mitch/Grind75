'''Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Helper function to print the tree
def print_tree(root):
    queue = [root]
    tree_list = []
    while len(queue) > 0:
        node = queue.pop(0)
        tree_list.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return tree_list

def bst_lca(root, p, q):
    small, big = (p.val, q.val) if p.val < q.val else (q.val, p.val)
    val = root.val
    # Base case returns node value if it's between p & q
    if small <= val and big >= val:
        return root
    # Recurse right or left depending on relationship between node value and p & q
    if small < val and big < val:
        return bst_lca(root.left, p, q)
    else:
        return bst_lca(root.right, p, q)

# TESTS

node1 = Node(6)
node2 = Node(2)
node3 = Node(8)
node4 = Node(0)
node5 = Node(4)
node6 = Node(3)
node7 = Node(5)
node8 = Node(7)
node9 = Node(9)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node5.left = node6
node5.right = node7
node3.left = node8
node3.right = node9

print(print_tree(node1))

print(bst_lca(node1, node2, node3).val)
# >>6
print(bst_lca(node1, node2, node5).val)
# >>2

