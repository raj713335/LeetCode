# https://leetcode.com/problems/minimum-positive-sum-subarray/description/

import math

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        minimun_positive_sum = math.inf

        for i in range(l, r+1):
            for j in range(0, len(nums)):
                if len(nums[j:j+i]) == i:
                    temp_sum = sum(nums[j:j+i])
                    if temp_sum < minimun_positive_sum and temp_sum > 0:
                        minimun_positive_sum = temp_sum

        if minimun_positive_sum == math.inf:
            return -1
        else:
            return minimun_positive_sum
        
