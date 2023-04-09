# https://leetcode.com/problems/minimize-maximum-of-array/description/

import math

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        res = nums[0]
        total = nums[0]
        count = 1

        for i in range(1, len(nums)):
            count += 1
            total = total + nums[i]
            value = math.ceil(total / count)
            res = max(res, value)

        return res
