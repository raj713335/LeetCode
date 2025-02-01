# https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/description/

class Solution:
    def findValidPair(self, s: str) -> str:
        
        dictx = {}
        
        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
                
                
        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]
            if a != b and dictx[a] == int(a) and dictx[b] == int(b):
                return a + b
                
        return ""
        
