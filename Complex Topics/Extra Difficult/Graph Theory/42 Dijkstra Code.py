# Time Complexity: O(E. log V) || O(n × T × log(n × T) + m × T) 
# Space Complexity: O(n × T + m)


import heapq
from collections import defaultdict

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:

        n = len(passingFees)

        # Build graph: city -> [(neighbor, time)]
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # (cost, city, time)
        pq = [(passingFees[0], 0, 0)]
        
        # minTime[i] = minimum time we reached city i
        minTime = [float('inf')] * n
        minTime[0] = 0

        while pq:
            cost, city, time = heapq.heappop(pq)

            if city == n - 1:
                return cost
            
            for nei, t in graph[city]:
                newTime = time + t
                newCost = cost + passingFees[nei]

                if newTime <= maxTime and newTime < minTime[nei]:
                    minTime[nei] = newTime
                    heapq.heappush(pq, (newCost, nei, newTime))

        return -1
        
