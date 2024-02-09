import uuid
import networkx as nx
import matplotlib.pyplot as plt
import math


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Placeholder for the left child node
        self.right = None  # Placeholder for the right child node
        self.val = key  # The value of the node
        self.color = color  # The color of the node for visualization purposes
        self.id = str(uuid.uuid4())  # A unique identifier for each node


# Function to add edges between nodes in a graph recursively
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Add a node to the graph with its unique ID, color, and value as label
        graph.add_node(node.id, color=node.color, label=node.val)
        # If the node has a left child, add an edge and calculate its position
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer  # Calculate the x position for the left child
            # Set the position of the left child
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        # If the node has a right child, add an edge and calculate its position
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer  # Calculate the x position for the right child
            # Set the position of the right child
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph  # Return the graph with all nodes and edges added


# Function to draw a binary heap
def draw_heap(heap):
    tree = nx.DiGraph()
    n = len(heap)  # The number of nodes in the heap
    positions = {}  # Dictionary to hold node positions

    for i in range(n):
        # Add heap nodes to the graph
        tree.add_node(i, label=heap[i], color="skyblue")
        # Calculate positions for each node to visually represent a binary heap
        # Calculate the level of the node
        level = int(math.floor(math.log2(i+1)))
        max_nodes_in_level = 2 ** level  # Maximum nodes that can be at the current level
        # Calculate x position within the current level
        x_position = i + 1 - max_nodes_in_level
        # Adjust x position for spacing and centering
        x_position = (x_position * 2 + 1) * \
            (2 ** (math.floor(math.log2(n+1)) - level) / 2.0)
        # The y position is negative the level (to go downwards)
        y_position = -level
        positions[i] = (x_position, y_position)  # Assign position for the node

        # If the node is not the root, add an edge to its parent
        if i != 0:
            parent = (i - 1) // 2  # Calculate the parent's index
            tree.add_edge(parent, i)  # Add the edge to the graph

    # Get the colors and labels for each node for visualization
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    # Create a figure and draw the graph using matplotlib
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=positions, labels=labels,
            arrows=False, node_size=2500, node_color=colors)
    plt.show()  # Display the drawn graph


# Example heap array
heap = [10, 7, 5, 4, 6, 2]
draw_heap(heap)  # Visualize the heap
