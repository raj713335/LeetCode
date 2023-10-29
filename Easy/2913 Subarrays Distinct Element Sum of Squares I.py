# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/


class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        sumx = 0

        for i in range(0, len(nums)):
            for j in range(i, len(nums)+1):
                temp = nums[i:j]
                lenx = len(set(temp))
                sumx += lenx ** 2
        
        return sumx

        
