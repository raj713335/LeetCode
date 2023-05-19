# https://leetcode.com/problems/find-xor-beauty-of-array/description/


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:

        res = 0

        for i in range(0, len(nums)):
            res = res ^ nums[i]

        return res
