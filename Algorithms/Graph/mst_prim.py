'''
Prim's Algorithm is a greedy approach,
which includes selecting minimum weight edges and expanding MST from a starting vertex, choosing nearest vertices.

Kruskal does sorting on edges, so if the graph is dense, Prim's algo is better
'''

import heapq

def prim(graph, start=0):
    
    # The priority queue to select the edge with the smallest weight
    min_heap = [(0, start, -1)]  # (weight, node, previous_node)
    mst_set = set()  # To keep track of nodes included in the MST
    mst_edges = []  # To store the edges in the MST
    total_weight = 0  # To keep track of the total weight of the MST

    while min_heap:
        weight, node, prev_node = heapq.heappop(min_heap)
        
        # Skip if the node is already included in the MST
        if node in mst_set:
            continue
        
        # Include the node in the MST
        mst_set.add(node)
        total_weight += weight
        
        # Add the edge to the MST (skip the first node)
        if prev_node != -1:
            mst_edges.append((prev_node, node, weight))

        # Explore the neighbors of the current node
        for neighbor, edge_weight in graph[node]:
            if neighbor not in mst_set:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))  # Update the previous node to current

    return mst_edges, total_weight

# Example usage
graph = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)]
}

mst_edges, total_weight = prim(graph, start=0)
print("Edges in MST:", mst_edges)
print("Total weight of MST:", total_weight)
