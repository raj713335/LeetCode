# https://leetcode.com/problems/k-closest-points-to-origin/description/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []
        res = []

        count = 0

        for num in points:
            heapq.heappush(min_heap, ((num[0] ** 2) +  (num[1] ** 2), count ))
            count += 1

        while k > 0 and heapq:
            value, index = heapq.heappop(min_heap)
            res.append(points[index])
            k -= 1

        return res
        
