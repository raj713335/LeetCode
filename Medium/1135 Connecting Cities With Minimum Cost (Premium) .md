# https://leetcode.com/problems/connecting-cities-with-minimum-cost/description/

### Problem Explanation: Leetcode 1135 - Connecting Cities With Minimum Cost

**Problem Statement:**

You are given an undirected graph with `n` cities (numbered from 1 to `n`), and a list of roads. Each road is represented as `[city1, city2, cost]`, where `city1` and `city2` are two cities, and `cost` is the cost to travel between these two cities. 

Your task is to find the minimum cost to connect all cities together such that every city is reachable from any other city. In other words, you need to connect all the cities in the form of a Minimum Spanning Tree (MST), and the problem asks for the total minimum cost to connect all the cities.

- **Input:**
  - `n`: an integer, representing the number of cities.
  - `roads`: a list of lists, where each list `[city1, city2, cost]` represents a road between `city1` and `city2` with the travel cost `cost`.

- **Output:**
  - The minimum cost to connect all cities together. If it is not possible to connect all cities, return `-1`.

### Approach:

This problem can be solved using **Kruskal's Algorithm** for finding the **Minimum Spanning Tree (MST)**. The MST of a graph is a subset of the edges that connects all the vertices with the minimum possible total edge weight, without forming any cycles.

Steps to solve the problem:
1. **Sort all the roads by cost**: To implement Kruskal’s algorithm, we first sort the edges in ascending order of their weights (cost).
2. **Union-Find (Disjoint Set)**: We use a union-find data structure to detect and avoid cycles while adding edges to the MST. This ensures that the selected edges do not form any cycle.
3. **Select edges until all cities are connected**: We keep adding edges to the MST until we have `n-1` edges (which is the number of edges needed to connect `n` cities).
4. If we can't connect all cities (i.e., fewer than `n-1` edges are added), return `-1`.

### Code Implementation:

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

def minimumCost(n, roads):
    # Sort roads by cost
    roads.sort(key=lambda x: x[2])
    
    # Create UnionFind instance for n cities
    uf = UnionFind(n)
    
    total_cost = 0
    edges_used = 0
    
    # Process each road
    for city1, city2, cost in roads:
        # Union the two cities if they are not already connected
        if uf.union(city1 - 1, city2 - 1):
            total_cost += cost
            edges_used += 1
        
        # If we have n-1 edges, all cities are connected
        if edges_used == n - 1:
            return total_cost
    
    # If we can't connect all cities, return -1
    return -1
```

### Explanation of the Code:

1. **UnionFind Class**: 
   - The `UnionFind` class helps to keep track of the connected components in the graph using the **Union-Find (Disjoint Set Union)** data structure.
   - `find(x)`: Returns the root of the component that contains `x`. It uses **path compression** to flatten the tree structure for faster future lookups.
   - `union(x, y)`: Merges the components containing `x` and `y`. It uses **union by rank** to keep the tree balanced, ensuring better time complexity.

2. **minimumCost Function**:
   - **Sort the roads**: We first sort the roads by their cost (third element of each road).
   - **Union-Find Initialization**: We initialize a `UnionFind` instance for `n` cities.
   - **Process Roads**: We iterate over the sorted roads and try to add each road to the MST. If the cities are not already connected, we connect them using `union()` and update the total cost and the number of edges used.
   - If we successfully use `n-1` edges, we return the total cost. If after processing all roads we don’t have `n-1` edges, it means it is not possible to connect all cities, so we return `-1`.

### Time Complexity:
- Sorting the roads takes \(O(E \log E)\), where \(E\) is the number of roads.
- Each `union` and `find` operation takes nearly constant time, \(O(\alpha(n))\), where \(\alpha(n)\) is the inverse Ackermann function. For practical purposes, \(\alpha(n)\) is very small and can be considered as a constant.
- Thus, the overall time complexity is \(O(E \log E)\).

### Space Complexity:
- The space complexity is \(O(n + E)\), where \(n\) is the number of cities and \(E\) is the number of roads, due to the storage required for the union-find structure and the input roads.

---

### README File

Here’s a sample README file to accompany the code:

---

# Leetcode 1135 - Connecting Cities With Minimum Cost

## Problem Description:

Given an undirected, connected graph with `n` cities, represented by a list of roads, each road is described by an array `[city1, city2, cost]` where `city1` and `city2` are the cities connected by the road and `cost` is the cost to travel between them. The goal is to find the minimum cost to connect all cities using a **Minimum Spanning Tree (MST)**.

### Input:
- `n`: Number of cities (1 ≤ n ≤ 100)
- `roads`: List of lists where each list `[city1, city2, cost]` represents a road connecting two cities.

### Output:
- The minimum cost to connect all cities together. If it is not possible to connect all cities, return `-1`.

### Approach:
- This problem can be efficiently solved using **Kruskal’s Algorithm** to find the **Minimum Spanning Tree (MST)**.
- We use **Union-Find (Disjoint Set Union)** to manage the connected components and ensure that no cycles are formed while connecting cities.

### Code:

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

def minimumCost(n, roads):
    # Sort roads by cost
    roads.sort(key=lambda x: x[2])
    
    # Create UnionFind instance for n cities
    uf = UnionFind(n)
    
    total_cost = 0
    edges_used = 0
    
    # Process each road
    for city1, city2, cost in roads:
        # Union the two cities if they are not already connected
        if uf.union(city1 - 1, city2 - 1):
            total_cost += cost
            edges_used += 1
        
        # If we have n-1 edges, all cities are connected
        if edges_used == n - 1:
            return total_cost
    
    # If we can't connect all cities, return -1
    return -1
```

### Explanation:
- The `UnionFind` class is used to manage connected components while performing union and find operations.
- We use **Kruskal’s algorithm** to build the MST by sorting the roads based on their cost and progressively adding them to the MST using the `union()` method from `UnionFind`.
- If we manage to add `n-1` edges, the total cost is returned. If not, we return `-1`.

### Example:

**Input:**
```python
n = 3
roads = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
```

**Output:**
```python
6
```

### Time Complexity:
- Sorting the roads takes \(O(E \log E)\), where \(E\) is the number of roads.
- Each `union` and `find` operation takes nearly constant time, \(O(\alpha(n))\), where \(\alpha(n)\) is the inverse Ackermann function.

### Space Complexity:
- \(O(n + E)\) due to the space used by the UnionFind data structure and input storage.

---

This README provides a brief explanation and a working example for reference, making it easy to understand and implement the solution.
