# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/


import math

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        max_diff = abs(nums[0] - nums[-1])

        for i in range(0, len(nums)-1):
            temp = abs(nums[i] - nums[i+1])
            if temp > max_diff:
                max_diff = temp

        return max_diff
        
