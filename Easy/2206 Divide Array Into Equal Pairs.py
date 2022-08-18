# https://leetcode.com/problems/divide-array-into-equal-pairs/


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        dictx = {}
        
        for each in nums:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] -= 1
                if dictx[each] == 0:
                    del dictx[each]
                    
        if len(dictx) == 0:
            return True
        else:
            return False
            
        
