from collections import defaultdict

# This class represents an undirected graph using adjacency list representation
class Graph:

# Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    # Function to print a bfsTraversal of graph
    def bfsTraversal(self, vertex):

        # Mark all the vertices as not visited
        visited = set()

        # Create a queue for bfsTraversal
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(vertex)
        visited.add(vertex)

        while queue:

            # Dequeue a vertex from
            # Queue and print it
            vertex = queue.pop(0)
            print (vertex, end = " ")

            # Get all adjacent vertices of the dequeued vertex vertex.
            # If a adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[vertex]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

# Create a graph given
graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 1)
graph.addEdge(2, 5)
graph.addEdge(3, 6)

print ("Breadth First Traversal from 1 is : ")
graph.bfsTraversal(1)
