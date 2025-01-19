# https://leetcode.com/problems/sum-of-variable-length-subarrays/description/

class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        sumx = nums[0]

        for i in range(1, len(nums)):
            start = max(0, i-nums[i])
            for j in range(start, i+1):
                sumx += nums[j]


        return sumx
