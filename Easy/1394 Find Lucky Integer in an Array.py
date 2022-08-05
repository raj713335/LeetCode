# https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        setx = sorted(set(arr))
        
        value = -1
        
        for each in setx:
            if arr.count(each) == each:
                value = each
                
        return value
            
        
