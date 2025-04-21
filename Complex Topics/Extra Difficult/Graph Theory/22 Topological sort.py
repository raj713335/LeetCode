# https://www.geeksforgeeks.org/problems/topological-sort/

from collections import defaultdict, deque

# BFS Solution

class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        
        adjancy_matrix = defaultdict(list)
        
        for u, v in edges:
            adjancy_matrix[u].append(v)
        
        indegree = defaultdict(int)
        
        
        for u, v in edges:
            indegree[v] += 1
            
        q = deque()
        
        
        for i in range(0, V):
            if indegree[i] == 0:
                q.append(i)
        
        topo_order = []       
        
        while q:
            
            node = q.popleft()
            topo_order.append(node)
            
            for next in adjancy_matrix[node]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    q.append(next)
        
        # If topo_order contains all nodes, return it
        if len(topo_order) == V:
            return topo_order
        else:
            return []  # Cycle exists (not possible in DAG by definition)
        
# DFS Solution

class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        visited = [False] * V
        topo_stack = []

        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            topo_stack.append(node)  # Post-order

        # Step 2: Visit all nodes
        for i in range(V):
            if not visited[i]:
                dfs(i)

        # Step 3: Reverse the result to get topological order
        topo_stack = topo_stack[::-1]
        
        # If topo_order contains all nodes, return it
        if len(topo_stack) == V:
            return topo_stack
        else:
            return []  # Cycle exists (not possible in DAG by definition)
        
        

