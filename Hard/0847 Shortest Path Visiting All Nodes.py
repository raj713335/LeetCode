# https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/

from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        n = len(graph)
        # Each state: (node, visited_mask)
        queue = deque()
        visited = set()

        # Initialize queue with all nodes as starting points
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))  # (node, visited_mask, path_length)
            visited.add((i, mask))
        
        target_mask = (1 << n) - 1

        while queue:
            node, mask, dist = queue.popleft()
            if mask == target_mask:
                return dist  # All nodes visited
            
            for nei in graph[node]:
                next_mask = mask | (1 << nei)
                if (nei, next_mask) not in visited:
                    visited.add((nei, next_mask))
                    queue.append((nei, next_mask, dist + 1))

        return -1  # should not happen since the graph is connected
        
