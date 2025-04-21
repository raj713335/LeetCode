Floyd-Warshall algorithm is used to compute shortest distance of any pair of nodes in a weight graph.

```c++
for k from 1 to |V|:
  for i from 1 to |V|:
    for j from 1 to |V|:
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

Though the runtime is O(|V|^3), actual runtime might be smaller than Dijkstra or other BFS algorithms.

# problems
* https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
* https://leetcode.com/problems/shortest-path-visiting-all-nodes/
