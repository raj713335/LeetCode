# https://leetcode.com/problems/maximum-sum-circular-subarray/description/


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        globalMax, globalMin = nums[0], nums[0]
        currMax, currMin = 0, 0
        total = 0

        for n in nums:
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)
            total += n
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)

        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax

