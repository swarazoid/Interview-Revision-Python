'''
This implementation implements Kahn's algorithm
'''

from collections import defaultdict, deque

def topological_sort(vertices, edges):
    # Step 1: Initialize graph structures
    adj_list = defaultdict(list)
    in_degree = {i: 0 for i in range(vertices)}

    # Step 2: Build the graph and calculate in-degrees
    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1

    # Step 3: Initialize the queue with nodes having in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])

    # Step 4: Perform topological sort
    topo_order = []

    while queue:
        current = queue.popleft()
        topo_order.append(current)

        # Reduce in-degree of neighbors and add to queue if in-degree becomes 0
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 5: Check if the graph is a DAG
    if len(topo_order) != vertices:
        raise ValueError("The graph is not a DAG (contains cycles)")

    return topo_order

# Driver Code
def main():
    # Example graph:
    # Number of vertices
    vertices = 6

    # Directed edges of the graph
    edges = [
        (5, 2),
        (5, 0),
        (4, 0),
        (4, 1),
        (2, 3),
        (3, 1)
    ]

    try:
        # Perform topological sort
        topo_order = topological_sort(vertices, edges)
        print("Topological Sort Order:", topo_order)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
