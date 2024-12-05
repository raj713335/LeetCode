import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        j = 0

        min_length = math.inf
        sumx = 0

        for i in range(0, len(nums)):
            sumx += nums[i]

            while sumx >= target:
                min_length = min(min_length, i - j + 1)
                sumx -= nums[j]
                j += 1

        if min_length == math.inf:
            return 0

        return min_length
