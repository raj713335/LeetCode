# https://leetcode.com/problems/3sum-closest/

import math

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        max_sum = math.inf
        res = 0
        nums = sorted(nums)
        for k in range(0, len(nums)):
            sums = nums[k]
            l, r = k + 1, len(nums) - 1
            while (l < r):
                sum_two = nums[k] + nums[l] + nums[r]
                temp = abs(target - sum_two)

                if temp < max_sum:
                    res = sum_two
                    max_sum = temp

                if sum_two < target:
                    l += 1
                elif sum_two > target:
                    r -= 1
                else:
                    return sum_two

        return res
