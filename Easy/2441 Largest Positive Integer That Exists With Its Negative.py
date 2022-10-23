# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        dictx = {}
        max_number = -1
        
        for i in range(0, len(nums)):
            dictx[nums[i]] = 1
            
        for each in nums:
            if each > 0:
                if (-1*each) in dictx:
                    if each > max_number:
                        max_number = each
                        
        return max_number
                
