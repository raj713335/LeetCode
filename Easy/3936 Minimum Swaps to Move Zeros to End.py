# https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/description/


class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:

        min_swaps = 0

        count_zero = nums.count(0)

        for i in range(len(nums) - count_zero, len(nums)):
            if nums[i] != 0:
                min_swaps += 1

        return min_swaps
        
