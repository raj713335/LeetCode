# https://leetcode.com/problems/find-k-closest-elements/description/

import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        max_heap = []

        for num in arr:
            dist = abs(num - x)
            heapq.heappush(max_heap, (-dist, -num))  # Max-heap trick

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        result = [-num for _, num in max_heap]
        return sorted(result)
        
