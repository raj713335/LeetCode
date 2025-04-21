# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

from collections import defaultdict, deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # dp[i][c] = max count of color c ending at node i
        dp = [[0] * 26 for _ in range(n)]
            
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        max_color = 0
        
        while q:
            
            node = q.popleft()
            visited += 1
            
            for nei in graph[node]:
                for c in range(26):
                    dp[nei][c] = max(dp[nei][c], dp[node][c] + (1 if c == ord(colors[nei]) - ord('a') else 0))
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        # If we visited all nodes, no cycle
        if visited != n:
            return -1  # cycle detected

        # Compute the max color count
        for row in dp:
            max_color = max(max_color, max(row))

        return max_color
