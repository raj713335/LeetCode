# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

def kruskal(n, edges, exclude_edge=None, include_edge=None):
    uf = UnionFind(n)
    mst_weight = 0
    edge_count = 0
    
    # If we are including an edge, add it first
    if include_edge is not None:
        a, b, weight = edges[include_edge]
        uf.union(a, b)
        mst_weight += weight
        edge_count += 1
    
    # Add edges from the sorted list (ignoring exclude_edge if needed)
    for i, (a, b, weight) in enumerate(edges):
        if i == exclude_edge:
            continue
        if uf.union(a, b):
            mst_weight += weight
            edge_count += 1
        if edge_count == n - 1:
            break
    
    # If we couldn't find n-1 edges, then it's not a valid MST
    if edge_count != n - 1:
        return float('inf')
    
    return mst_weight

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # Step 1: Sort edges by weight and map original indices
        indexed_edges = [(a, b, weight, i) for i, (a, b, weight) in enumerate(edges)]
        indexed_edges.sort(key=lambda x: x[2])  # Sort by weight
        
        # Re-index edges to make them easier to use in Kruskal's algorithm
        edges_sorted = [(a, b, weight) for a, b, weight, i in indexed_edges]
        edge_indices = [i for a, b, weight, i in indexed_edges]
        
        # Step 2: Find the weight of the MST of the entire graph
        mst_weight = kruskal(n, edges_sorted)
        
        critical_edges = []
        pseudo_critical_edges = []
        
        # Step 3: Check each edge
        for i in range(len(edges)):
            # Check if it's a critical edge
            if kruskal(n, edges_sorted, exclude_edge=i) > mst_weight:
                critical_edges.append(edge_indices[i])
            # Check if it's a pseudo-critical edge
            elif kruskal(n, edges_sorted, include_edge=i) == mst_weight:
                pseudo_critical_edges.append(edge_indices[i])
        
        return [critical_edges, pseudo_critical_edges]
        
