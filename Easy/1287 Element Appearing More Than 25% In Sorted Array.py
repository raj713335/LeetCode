# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        length = len(arr)/4
        
        dictx = {}
        
        for each in arr:
            if each not in dictx:
                dictx[each] = 1
                
                if dictx[each] > length:
                    return each
            else:
                dictx[each] += 1
            
                if dictx[each] > length:
                    return each
                
        return arr[0]
