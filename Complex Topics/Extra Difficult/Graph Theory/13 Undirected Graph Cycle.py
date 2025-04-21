# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/

# DFS Cycle Detection 

from collections import defaultdict

class Solution:
	def isCycle(self, V, edges):
		#Code here
		
		adjency_list = defaultdict(list)
		
		for u, v in edges:
		    adjency_list[u].append(v)
		    adjency_list[v].append(u)
		    
		visited = set()
		
		def dfs(node, adjency_list, visited, parent):
            visited.add(node)
            
            for next in adjency_list[node]:
                if next not in visited:
                    ans = dfs(next, adjency_list, visited, node)
                    if ans:
                        return True
                elif next in visited and next != parent:
                    return True
            return False
		
		for node in range(V):
		    if node not in visited:
		        ans = dfs(node, adjency_list, visited, -1)
		        if ans:
		            return True
		return False

# BFS Cycle detection

from collections import deque

def has_cycle_undirected(graph):
    visited = set()

    def bfs(start):
        queue = deque([(start, -1)])  # (node, parent)
        visited.add(start)

        while queue:
            node, parent = queue.popleft()

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    # If visited and not parent, a cycle exists
                    return True
        return False

    for node in graph:
        if node not in visited:
            if bfs(node):
                return True
    return False


