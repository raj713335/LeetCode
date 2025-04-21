# https://leetcode.com/problems/longest-cycle-in-a-graph/description/

from collections import defaultdict

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        adjency_list = defaultdict(list)

        n = len(edges)

        for i in range(n):
            if edges[i] != -1:
                adjency_list[i].append(edges[i])

        visited = set()
        current_path = [0] * (n)

        def dfs(node, adjency_list, visited, current_path, level):
            visited.add(node)
            level += 1
            current_path[node] = level

            for next in adjency_list[node]:
                if next not in visited:
                    result = dfs(next, adjency_list, visited, current_path, level)
                    if result != -1:
                        return result
                elif next in visited and current_path[next] != 0:
                    return current_path[node] - current_path[next] + 1
            
            current_path[node] = 0
            return -1

        max_distance = -1

        for node in range(n):
            if node not in visited:
                current_path = defaultdict(int)
                cycle_len = dfs(node, adjency_list, visited, current_path, 0)
                max_distance = max(max_distance, cycle_len)

        return max_distance
        
