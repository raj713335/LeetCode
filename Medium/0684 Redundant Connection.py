# https://leetcode.com/problems/redundant-connection/description/

from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def dfs(current, target, visited):
            if current == target:
                return True
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False

        graph = defaultdict(list)

        for u, v in edges:
            visited = set()
            # Check if u and v are already connected
            if u in graph and v in graph:
                if dfs(u, v, visited):
                    return [u, v]
            # If not connected, add edge
            graph[u].append(v)
            graph[v].append(u)

        return []

        
        
