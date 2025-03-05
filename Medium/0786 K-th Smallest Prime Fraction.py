# https://leetcode.com/problems/k-th-smallest-prime-fraction/description/

import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        max_heap = []
        index = 0

        for i in range(0, len(arr)-1):
            for j in range(i+1, len(arr)):
                heapq.heappush(max_heap, (-arr[i]/ arr[j], (arr[i], arr[j])))
                index += 1

                if index > k:
                    heapq.heappop(max_heap)


        return max_heap[0][1]        
