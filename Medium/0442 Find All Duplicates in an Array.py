# https://leetcode.com/problems/find-all-duplicates-in-an-array/


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        dictx = {}
        output = []
        
        for each in nums:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
                
        for key, value in dictx.items():
            if value >= 2:
                output.append(key)
                
        return output
                
        
        
