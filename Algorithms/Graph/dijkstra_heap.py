'''
Dijkstra Algorithm is a graph algorithm for finding the shortest path from 
a source node to all other nodes in a graph(single source shortest path).

It is a type of greedy algorithm. It only works on weighted graphs with positive weights. 
It has a time complexity of O(V^2) using the adjacency matrix representation of graph. 
The time complexity can be reduced to O((V+E)logV) using adjacency list representation of graph,
where E is the number of edges in the graph and V is the number of vertices in the graph.
'''

import heapq
from math import inf

def Dijkstra(graph, start):
    l = len(graph)
    
    # initialize all node distances as infinite
    dist = [inf for _ in range(l)]
    
    # set the distance of starting node as 0
    dist[start] = 0
    
    # create a list that indicates if a node is visited or not
    vis = [False for _ in range(l)]
    
    # creating a priority queue
    pqueue = [(0, start)]
    heapq.heapify(pqueue)
    
    # this while will run till there is some node to process 
    while len(pqueue) > 0:
        
        # we don't need the current node distance so use '_' as a variable for it.
        _, u = heapq.heappop(pqueue)
        
        # skip the node if it is visited
        if vis[u]:
            continue
            
        # set the current node as visited i.e True
        vis[u] = True
        
        for v, d in graph[u]:
            # now if the distance of the current node + the distance to the node we're visiting is less than the prior distance of the node we're visiting then update that distance and add that node to the priority queue
            if dist[u] + d < dist[v]:
                dist[v] = dist[u] + d
                heapq.heappush(pqueue, (dist[v], v))
    
    # now at last return the list which contains the shortest path to each node from that given node
    return dist

graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
}
print(Dijkstra(graph, 0))
