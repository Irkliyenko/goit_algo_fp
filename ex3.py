import heapq
import networkx as nx
import matplotlib.pyplot as plt


def graph_builder(input_dict):
    # Create a directed graph from the input dictionary
    G = nx.DiGraph(input_dict)
    # Adding edges with weights
    for node, neighbors in input_dict.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)
    pos = nx.spring_layout(G)
    # Drawing vertices
    nx.draw(G, pos, with_labels=True)
    # Getting edge weights and drawing them
    edge_weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights)
    plt.show()
    # Getting the shortest paths and lengths using NetworkX
    ctrl_shortest_paths = nx.single_source_dijkstra_path(G, source='A')
    ctrl_shortest_path_lengths = nx.single_source_dijkstra_path_length(
        G, source='A')
    return ctrl_shortest_path_lengths, ctrl_shortest_paths


def dijkstra_with_heap(graph, start):
    # Initializing distances and binary heap
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    min_heap = [(0, start)]  # (distance, vertex)

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        # Skip iteration if the distance in the heap is greater than the current distance
        if current_distance > distances[current_vertex]:
            continue

        # Update shortest path if a new shorter distance is found, and add to heap
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances


if __name__ == "__main__":

    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'D': 2},
        'D': {'B': 3, 'C': 2, 'E': 4},
        'E': {'D': 4}
    }

    # Building and showing the graph, and getting NetworkX Dijkstra results
    ctrl_shortest_path_lengths, ctrl_shortest_paths = graph_builder(graph)
    # Running custom Dijkstra algorithm
    res = dijkstra_with_heap(graph, 'A')

    print(
        f"Custom Dijkstra Algorithm:\n{res}\n\nNetworkX Dijkstra Algorithm (Path Lengths):\n{ctrl_shortest_path_lengths}\n\nNetworkX Dijkstra Algorithm (Paths):\n{ctrl_shortest_paths}")
