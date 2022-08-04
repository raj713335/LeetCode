# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = list(map(str, s.split(" ")))
        
        dictx = {}
        
        if len(s) != len(pattern):
            return False
        
        for i in range(0, len(s)):
            if pattern[i] not in dictx:
                dictx[pattern[i]] = s[i]
            else:
                if dictx[pattern[i]] != s[i]:
                    return False
                
        if len(set(dictx.values())) != len(dictx):
            return False
        return True
        
