# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:

        sumx = 0

        for i in range(0, len(nums)):
            if k == bin(i).count('1'):
                sumx += nums[i]

        return sumx
