# https://leetcode.com/problems/maximum-path-quality-of-a-graph/description/

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:

        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))

        n = len(values)
        max_quality = 0
        visited = [0] * n

        def dfs(node, time_spent, quality):
            nonlocal max_quality
            if time_spent > maxTime:
                return

            first_visit = visited[node] == 0
            visited[node] += 1

            if first_visit:
                quality += values[node]
            
            if node == 0:
                max_quality = max(max_quality, quality)

            for nei, t in graph[node]:
                dfs(nei, time_spent + t, quality)

            visited[node] -= 1  # Backtrack

        dfs(0, 0, 0)
        return max_quality
        
