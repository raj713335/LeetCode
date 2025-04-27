# Dijkstra's Algorithm

## 📖 Overview
Dijkstra's Algorithm is a famous **greedy algorithm** used to find the **shortest path** between a source node and all other nodes in a **weighted graph** with **non-negative edge weights**.

It is widely used in:
- **Routing protocols** (e.g., GPS navigation, network routing)
- **Graph-based problems** in competitive programming
- **Operations research** and **logistics**

---

## ⚙️ How It Works
1. **Initialize** the distance to the source node as 0 and to all other nodes as infinity.
2. **Use a priority queue (min-heap)** to greedily select the node with the smallest known distance.
3. **Update the distances** of neighboring nodes if a shorter path is found through the current node.
4. **Repeat** until all nodes have been visited or the target is reached.

---

## 🛠️ Pseudocode

```plaintext
function Dijkstra(graph, source):
    dist[source] = 0
    for each vertex v in graph:
        if v ≠ source:
            dist[v] = infinity
        add v to priority queue

    while priority queue is not empty:
        u = extract-min(priority queue)
        for each neighbor v of u:
            alt = dist[u] + weight(u, v)
            if alt < dist[v]:
                dist[v] = alt
                update priority queue with new distance
```

---

## 🧠 Key Concepts
- **Priority Queue**: Used to efficiently fetch the next node with the smallest tentative distance.
- **Greedy Approach**: Always picks the next closest node.
- **Works only with non-negative weights**.

---

## ⏱️ Time Complexity
| Data Structure | Time Complexity |
| :------------- | :-------------- |
| Simple Array Priority Queue | O(V²) |
| Binary Heap + Adjacency List | O((V + E) log V) |
| Fibonacci Heap | O(E + V log V) (theoretical, but rarely used in practice) |

Where:
- **V** = number of vertices
- **E** = number of edges

---

## 🧪 LeetCode Questions to Practice

| Problem | Link |
| :------ | :--- |
| 1. Network Delay Time | [LeetCode 743](https://leetcode.com/problems/network-delay-time/) |
| 2. Path With Minimum Effort | [LeetCode 1631](https://leetcode.com/problems/path-with-minimum-effort/) |
| 3. Minimum Cost to Connect All Points | [LeetCode 1584](https://leetcode.com/problems/min-cost-to-connect-all-points/) |
| 4. Cheapest Flights Within K Stops | [LeetCode 787](https://leetcode.com/problems/cheapest-flights-within-k-stops/) |
| 5. The Maze II | [LeetCode 505](https://leetcode.com/problems/the-maze-ii/) |
| 6. Shortest Path Visiting All Nodes | [LeetCode 847](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) (BFS + Bitmask, but conceptually close) |
| 7. Dijkstra Variant - Minimum Cost to Reach Destination in Time | [LeetCode 1928](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/) |

---

## ✍️ Notes for Interviews
- Always ask if the graph is **directed or undirected**.
- Clarify if **negative weights** exist (if yes, Dijkstra is **not** the right algorithm; use **Bellman-Ford**).
- Use **heap** for optimal performance.
- Think about **early stopping** if you only need shortest distance to a **target node**, not all nodes.

---

## 📚 Further Reading
- [Dijkstra’s Algorithm - GeeksforGeeks](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
- [MIT OpenCourseWare - Shortest Paths](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/lecture-16-dijkstra/)

