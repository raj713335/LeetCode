# https://leetcode.com/problems/find-the-shortest-superstring-ii/description/

class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:

        n, m = len(s1), len(s2)

        if n > m:                           # <-- 1)
            s1, s2, n = s2, s1, m           #

        if s1 in s2: return s2              # <-- 2)

        for i in range(1, n):
            if s1[i:] == s2[:n-i]:          #
                return s1[:i] + s2          # <-- 3)
            if s2[-i:] == s1[:i]:           #
                return s2 + s1[i:]          #

        return s1 + s2
        
