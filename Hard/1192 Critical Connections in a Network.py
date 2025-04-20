# https://leetcode.com/problems/critical-connections-in-a-network/description/


# Solved using Tarjans algorithm for bridge
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        discovery = [-1] * n
        low = [-1] * n
        time = [0]
        res = []

        def dfs(u, parent):
            discovery[u] = low[u] = time[0]
            time[0] += 1

            for v in graph[u]:
                if v == parent:
                    continue
                if discovery[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > discovery[u]:
                        res.append([u, v])
                else:
                    low[u] = min(low[u], discovery[v])

        dfs(0, -1)
        return res
        
