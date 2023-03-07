# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/


import math

class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        nums = sorted(nums)

        mid = len(nums)//2

        ans = 0
        for j in range(0, len(nums)):
            ans += abs(nums[mid]-nums[j])

        return ans
