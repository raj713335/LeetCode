# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        count = 0

        while len(nums) != len(set(nums)):
            nums = nums[3:]
            count += 1

        return count
