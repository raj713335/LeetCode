# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        n1 = len(s)
        n2 = len(t)

        if n1 == 0:
            return True

        i = 0
        j = 0

        while j < n2 and i < n1:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        if i == n1:
            return True
        else:
            return False
        
