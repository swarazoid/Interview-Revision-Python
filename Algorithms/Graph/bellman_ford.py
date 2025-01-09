"""
The Bellman-Ford algorithm is used to find the shortest path from a single source vertex
to all other vertices in a weighted graph. It can handle graphs with negative weight edges,
but it detects negative weight cycles.

- Time Complexity: O( |V| * |E| ) 
- Space Complexity: O( |V| + |E| )
"""

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

def bellman_ford(vertices, edges, source):
    # Step 1: Initialize distances
    distance = [float('inf')] * vertices
    distance[source] = 0

    # Step 2: Relax edges |V| - 1 times
    for _ in range(vertices - 1):
        for edge in edges:
            if distance[edge.source] != float('inf') and distance[edge.source] + edge.weight < distance[edge.destination]:
                distance[edge.destination] = distance[edge.source] + edge.weight

    # Step 3: Check for negative weight cycles
    for edge in edges:
        if distance[edge.source] != float('inf') and distance[edge.source] + edge.weight < distance[edge.destination]:
            print("Graph contains a negative weight cycle")
            return None

    return distance

# Example usage
edges = [
    Edge(0, 1, 4),
    Edge(0, 2, 5),
    Edge(1, 2, -3),
    Edge(1, 3, 2),
    Edge(2, 3, 6)
]

vertices = 4  # Number of vertices
source = 0  # Source vertex

shortest_distances = bellman_ford(vertices, edges, source)

if shortest_distances:
    print("Vertex Distance from Source")
    for i, d in enumerate(shortest_distances):
        print(f"{i} \t {d}")
