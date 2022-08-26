# https://leetcode.com/problems/single-number-ii/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dictx = {}
        
        for each in nums:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
                
        for key, value in dictx.items():
            if value == 1:
                return key
        
