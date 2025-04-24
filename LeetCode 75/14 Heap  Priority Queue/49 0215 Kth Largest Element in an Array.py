# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        res = []

        for i in range(0, len(nums)):

            heapq.heappush(res, nums[i])

            if i >= k:
                heapq.heappop(res)

        return res[0]
