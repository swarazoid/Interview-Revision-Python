from collections import defaultdict

def detect_cycle_undirected(vertices, edges):
    def dfs(node, parent):
        visited[node] = True
        
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        
        return False

    # Build graph
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  # Add both directions for undirected graph

    visited = [False] * vertices

    # Run DFS for each unvisited node
    for node in range(vertices):
        if not visited[node]:
            if dfs(node, -1):
                return True

    return False

# Example Usage
vertices = 5
edges = [(0, 1), (1, 2), (2, 0), (3, 4)]  # This graph contains a cycle
print("Cycle detected in undirected graph:", detect_cycle_undirected(vertices, edges))
