# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/description/


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        max_sum = 0

        prefix_max = nums[0]
        max_diff = 0

        for k in range(1, len(nums)):
            max_sum = max(max_sum, max_diff * nums[k])
            max_diff = max(max_diff, prefix_max - nums[k])
            prefix_max = max(prefix_max, nums[k])

        return max_sum
