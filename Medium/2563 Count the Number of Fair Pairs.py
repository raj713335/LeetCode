# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n):
            low = lower - nums[i]
            high = upper - nums[i]

            # We want j > i, so search in nums[i+1:]
            left = bisect_left(nums, low, i + 1, n)
            right = bisect_right(nums, high, i + 1, n)

            count += right - left

        return count
