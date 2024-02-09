import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


# Node class definition with additional attributes for left, right children, value, color, and a unique ID
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = None  # Initially no color, will be set during traversal
        self.id = str(uuid.uuid4())


# Function to recursively add nodes and edges to a NetworkX graph
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Add the current node to the graph
        graph.add_node(node.id, color=node.color, label=node.val)
        # Position the node for visualization
        pos[node.id] = (x, y)
        # Recursively add left and right children
        if node.left:
            graph.add_edge(node.id, node.left.id)
            add_edges(graph, node.left, pos, x=x-1 /
                      2**layer, y=y-1, layer=layer+1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            add_edges(graph, node.right, pos, x=x+1 /
                      2**layer, y=y-1, layer=layer+1)
    return graph


# Function to calculate color based on traversal order
def get_color(index, total_nodes):
    # Calculate intensity to create varying shades of blue, avoiding white color
    intensity = 240 - int((index / total_nodes) * 240)
    return f"#{intensity:02x}{intensity:02x}{240:02x}"


# Function to perform BFS traversal and color nodes
def bfs_coloring(root, total_nodes):
    queue = deque([root])
    index = 0
    while queue:
        node = queue.popleft()
        # Assign color based on the order in BFS
        node.color = get_color(index, total_nodes)
        index += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Function to perform DFS traversal and color nodes
def dfs_coloring(node, index, total_nodes):
    if node:
        # Assign color based on the order in DFS
        node.color = get_color(index[0], total_nodes)
        index[0] += 1
        # Recursively apply to left and right children
        dfs_coloring(node.left, index, total_nodes)
        dfs_coloring(node.right, index, total_nodes)


# Function to draw the tree with colored nodes
def draw_tree(tree_root, traversal_type='bfs'):
    tree = nx.DiGraph()
    pos = {}
    total_nodes = count_nodes(tree_root)
    # Apply coloring based on the selected traversal type
    if traversal_type == 'bfs':
        bfs_coloring(tree_root, total_nodes)
    else:
        dfs_coloring(tree_root, [0], total_nodes)
    tree = add_edges(tree, tree_root, pos)
    # Extract color and labels for visualization
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


# Helper function to count the total number of nodes in the tree
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


# Create and visualize the binary tree using BFS and DFS
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Draw the tree using BFS traversal
draw_tree(root, traversal_type='bfs')

# Draw the tree using DFS traversal
draw_tree(root, traversal_type='dfs')
