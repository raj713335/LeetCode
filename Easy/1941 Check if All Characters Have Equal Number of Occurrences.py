# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        dictx = {}
        
        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
        
        val = set(dictx.values())
        
        if len(val) == 1:
            return True
        else:
            return False
        
        
        
