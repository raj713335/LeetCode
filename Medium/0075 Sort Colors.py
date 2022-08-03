# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        dictx = {}
        output = []
        
        for each in nums:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
                
        for each in sorted(dictx.keys()):
            output.extend([each]*dictx[each])
            
        nums[:] = output
        
        
                
        
