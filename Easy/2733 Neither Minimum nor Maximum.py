# https://leetcode.com/problems/neither-minimum-nor-maximum/


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:

        nums = sorted(list(set(nums)))

        if len(nums) < 3:
            return -1
        else:
            return nums[1]
