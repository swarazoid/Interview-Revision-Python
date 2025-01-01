from collections import defaultdict

def topological_sort(vertices, edges):
    # Step 1: Initialize graph structures
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)

    # Step 2: Perform DFS and record post-order
    visited = [False] * vertices
    rec_stack = [False] * vertices  # Tracks nodes in the current recursion stack
    topo_stack = []

    def dfs(node):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:  # Cycle detected
                return True

        rec_stack[node] = False
        topo_stack.append(node)
        return False

    # Step 3: Call DFS for all unvisited nodes
    for node in range(vertices):
        if not visited[node]:
            if dfs(node):
                raise ValueError("The graph contains a cycle")

    # Step 4: Reverse the post-order stack to get topological order
    return topo_stack[::-1]

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
