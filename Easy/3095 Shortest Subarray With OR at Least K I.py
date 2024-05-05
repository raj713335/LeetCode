# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/description/


import math 

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        acc = nums

        for i in range(1,len(nums)+1):

            if max(acc) >= k: return i
            acc = [x|y for x,y in zip(acc, nums[i:])]
 
        return -1
        
