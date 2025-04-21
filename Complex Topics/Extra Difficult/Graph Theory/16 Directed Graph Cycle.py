# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

from collections import defaultdict

class Solution:
    def isCycle(self, V, edges):
        
        adjency_list = defaultdict(list)
		
        for u, v in edges:
            adjency_list[u].append(v)
            
        visited = set()
        current_path = set()

        def dfs(node, adjency_list, visited, current_path):
            visited.add(node)
            current_path.add(node)
            
            for next in adjency_list[node]:
                if next not in visited:
                    ans = dfs(next, adjency_list, visited, current_path)
                    if ans:
                        return True
                elif next in visited and next in current_path:
                    return True
                    
            current_path.remove(node)
            return False

        for node in range(V):
            if node not in visited:
                ans = dfs(node, adjency_list, visited, current_path)
                if ans:
                    return True
        return False

