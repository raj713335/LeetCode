# https://leetcode.com/problems/shortest-cycle-in-a-graph/description/


from collections import defaultdict

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        shortest = float('inf')

        for start in range(n):
            dist = [-1] * n
            parent = [-1] * n
            q = deque()
            q.append(start)
            dist[start] = 0

            while q:
                node = q.popleft()
                for neighbor in adj[node]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[node] + 1
                        parent[neighbor] = node
                        q.append(neighbor)
                    elif parent[node] != neighbor:
                        # Cycle found
                        cycle_length = dist[node] + dist[neighbor] + 1
                        shortest = min(shortest, cycle_length)

        return shortest if shortest != float('inf') else -1
