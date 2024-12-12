# https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = list(map(str, s.split(" ")))

        if len(s) != len(pattern):
            return False
        
        dictx1 = {}
        dictx2 = {}
        
        for i in range(0, len(pattern)):
            if pattern[i] not in dictx1:
                dictx1[pattern[i]] = s[i]
            else:
                if dictx1[pattern[i]] != s[i]:
                    return False
            if s[i] not in dictx2:
                dictx2[s[i]] = pattern[i]
            else:
                if dictx2[s[i]] != pattern[i]:
                    return False

        return True
        
