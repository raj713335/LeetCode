# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        dictx = {}
        value = 0
        
        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
                
        for each in t:
            if each not in dictx:
                dictx[each] = -1
            else:
                dictx[each] -= 1
                
        for key, val in dictx.items():
            value += abs(val)
        
        
        if value % 2 == 0:
            return value//2
        else: 
            return (value//2)+1
            
