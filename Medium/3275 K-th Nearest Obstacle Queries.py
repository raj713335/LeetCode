# https://leetcode.com/problems/k-th-nearest-obstacle-queries/description/

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        
        n = len(queries)
        pq = []
        res = []
        for i in range(n):
            sum_val = abs(queries[i][0]) + abs(queries[i][1])
            heapq.heappush(pq, -sum_val)
            if len(pq) > k:
                heapq.heappop(pq)
            res.append(-pq[0] if len(pq) == k else -1)
        return res
