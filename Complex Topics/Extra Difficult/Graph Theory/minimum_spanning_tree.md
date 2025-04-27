# Minimum Spanning Tree
A spanning tree (ST) is a subgraph where all vertices are connected with minimum number of edges. A minimum spanning tree (MST) is a ST of a weighted undirected graph, where the total edge weight is minimum. There are mainly two algorithms to find a MST of a graph, ```Kruskal's Algorithm with Union-find``` and ```Prim's algorithm with heap```.

## Cut & Cut Property
In Graph theory, a “cut” is a partition of vertices in a “graph” into two disjoint subsets. From wiki, the "cut property" is defined as:   
```
For any cut C of the graph, if the weight of an edge E in the cut-set of C is strictly smaller than the weights of all other edges of the cut-set of C, then this edge belongs to all MSTs of the graph.
```
Taking advantage of the cut property, we have the above mentioned two algorithms. 

## Kruskal's Algorithm with Union-find
```
1. Sort the edges in acsending order according to their costs.    
2. Define the Union-find data structure.   
3. For each edge:   
    x, y, cost = edge   
    root_x, root_y = find(x), find(y)   
    if root_x == root_y:   
        continue   
    union(x, y)   
4. Check if an MST is formed   
```
Time complexity is O(ElogE + E&alpha;(V)) = O(ElogE). See [here](https://github.com/shiwentao00/Python-cheat-sheet/blob/main/graph/kruskal_algorithm.py) for an example implementation.   
Examples:    
1. Leetcode 1135. Connecting Cities With Minimum Cost. [here](https://github.com/raj713335/LeetCode/blob/dev/Medium/1135%20Connecting%20Cities%20With%20Minimum%20Cost%20(Premium)%20.md)
2. Leetcode 1584. Min Cost to Connect All Points. [here](https://leetcode.com/problems/min-cost-to-connect-all-points/description/)
3. Leetcode 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree [here](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/)

## Prim's algorithm with heap
```
1. Form a graph data structure so that we can find the neighbors of a node in O(1).    
2. Put first node in ```visited``` and other nodes in ```unvisited```, and put all the edges from first node into a heap.   
3. while heap:   
    pop out an edge from heap    
        if the edge is connecting the current cut and its outside (connecting visited and unvisited):   
            add the destination to ```visited```, remove the destination from ```unvisited```   
            add all edges from destination to the heap   
4. Check if an MST is formed   
```
Time complexity is O(E⋅logV). See [here](https://github.com/shiwentao00/Python-cheat-sheet/blob/main/graph/prim_algorithm.py) for an example implementation.
