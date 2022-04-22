# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        dictx = {}
        
        for each in nums:
            dictx[each]=1
            
        for i in range(1, 2**31):
            if i not in dictx:
                return i
        
