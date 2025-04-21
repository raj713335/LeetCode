# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # Step 1: Initialize distance matrix
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        # Step 2: Fill in direct edge weights
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Step 3: Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Step 4: Count reachable cities and find the desired one
        result_city = -1
        min_reachable = n  # worst case, all cities are reachable
        
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1
            # if tie on count, prefer city with higher index
            if count <= min_reachable:
                min_reachable = count
                result_city = i
        
        return result_city
        
