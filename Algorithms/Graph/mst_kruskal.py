'''
The Kruskal's algorithm is a Greedy Algorithm. 
The greedy choice is to pick the smallest weight edge that does not cause a cycle in the MST constructed so far.

Adjacency Matrix Representation:
- Time Complexity: O(V2)
- Space Complexity: O(V2)

Adjacency List Representation:
- Time Complexity: O(ElogE + ELogV)
- Space Complexity: O(V + E)
'''

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(vertices, edges):
    # Step 1: Sort edges by weight
    edges.sort(key=lambda x: x[2])
    print(edges)

    # Step 2: Initialize Union-Find and MST result
    uf = UnionFind(vertices)
    mst = []
    mst_cost = 0

    # Step 3: Process edges
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            mst_cost += weight

    return mst, mst_cost

# Driver Code
def main():
    vertices = 6
    edges = [
        (0, 1, 4),
        (0, 2, 4),
        (1, 2, 2),
        (1, 0, 4),
        (2, 3, 3),
        (2, 5, 2),
        (2, 4, 4),
        (3, 4, 3),
        (5, 4, 3)
    ]

    mst, mst_cost = kruskal(vertices, edges)
    print("Minimum Spanning Tree:", mst)
    print("Total Cost of MST:", mst_cost)

if __name__ == "__main__":
    main()
