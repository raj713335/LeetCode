# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dictx = {}
        
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
            
        
        if min(dictx.values()) == 0 and max(dictx.values())==0:
            return True
        else:
            return False
        
