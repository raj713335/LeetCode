# https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dictx1 = {}
        dictx2 = {}

        for i in range(0, len(s)):
            if t[i] not in dictx1:
                dictx1[t[i]] = s[i]
            else:
                if dictx1[t[i]] != s[i]:
                    return False
            if s[i] not in dictx2:
                dictx2[s[i]] = t[i]
            else:
                if dictx2[s[i]] != t[i]:
                    return False

        return True
        
