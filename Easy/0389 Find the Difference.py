# https://leetcode.com/problems/find-the-difference/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        dictx = {}
        
        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
                
        for each in t:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] -= 1
                
        print(dictx)
                
        for key, value in dictx.items():
            if value != 0:
                return key
                
        
        
