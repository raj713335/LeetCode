# https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
            
        dictx = {}

        for i in range(0, len(s)):
            if s[i] not in dictx:
                dictx[s[i]] = 1
            else:
                dictx[s[i]] += 1


        for i in range(0, len(t)):
            if t[i] in dictx and dictx[t[i]] > 0:
                dictx[t[i]] -= 1
            else:
                return False   

        return True
        
