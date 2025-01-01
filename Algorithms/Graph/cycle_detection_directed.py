from collections import defaultdict

def detect_cycle_directed(vertices, edges):
    def dfs(node):
        visited[node] = True
        rec_stack[node] = True
        
        # Explore neighbors
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True
        
        rec_stack[node] = False  # Backtrack
        return False
    
    # Build graph
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
    
    visited = [False] * vertices
    rec_stack = [False] * vertices

    # Run DFS for each unvisited node
    for node in range(vertices):
        if not visited[node]:
            if dfs(node):
                return True

    return False

# Example Usage
vertices = 4
edges = [(0, 1), (1, 2), (2, 0), (3, 2)]  # This graph contains a cycle
print("Cycle detected in directed graph:", detect_cycle_directed(vertices, edges))
