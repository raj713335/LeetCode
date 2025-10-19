# https://leetcode.com/problems/smallest-missing-multiple-of-k/description/

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        dictx = {}

        for i in range(0, len(nums)):
            dictx[nums[i]] = 1

        for i in range(1, len(nums)+2):
            if k * i not in dictx.keys():
                return (k*i)
        
