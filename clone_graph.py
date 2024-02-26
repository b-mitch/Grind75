'Given a reference of a node in a connected undirected graph, Return a deep copy (clone) of the graph.'

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def clone_graph(node):
    # Check if node is none or has no neighbors
    if not node:
        return node
    if not len(node.neighbors):
        return Node(node.val)
    # Set up variables to traverse with stack and create adjacency list
    adj_list, stack, visited = [], [node], [node]
    while len(stack):
        current = stack.pop()
        # Add all current, neighbor pairs to the adjacency list
        for neighbor in current.neighbors:
            adj_list.append([current.val, neighbor.val])
            # Add to stack if not visited
            if neighbor not in visited:
                stack.append(neighbor)
                visited.append(neighbor)
    # Create dictionary to save new graph nodes
    new_graph = dict()
    # Iterate adjacency list, creating new nodes and adding neighbors
    for val1, val2 in adj_list:
        # Create new nodes if they have not yet been created
        if val1 not in new_graph:
            new_graph[val1] = Node(val1)
        if val2 not in new_graph:
            new_graph[val2] = Node(val2)
        # Add neighbor
        new_graph[val1].neighbors.append(new_graph[val2])
    # The first node is the node at key of 1
    return new_graph[1]

# TESTS

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node9 = Node(9)

node1.neighbors = [node2, node3]
node2.neighbors = [node1, node4]
node3.neighbors = [node1, node5]
node4.neighbors = [node2, node5]
node5.neighbors = [node3, node4]

print(node1)
print(clone_graph(node1))
# >>clone of node1

print(node9)
print(clone_graph(node9))
# >>clone of node9