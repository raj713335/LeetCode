# https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/

import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        sumx = 0
        nums = [-n for n in nums]

        heapq.heapify(nums)

        for i in range(k):
            val = -heapq.heappop(nums)
            sumx += val
            heapq.heappush(nums, -math.ceil(val/3))

        return sumx

        
