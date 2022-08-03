# https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        dictx = {}
        
        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                return each
        
