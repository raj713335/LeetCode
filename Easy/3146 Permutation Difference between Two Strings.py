# https://leetcode.com/problems/permutation-difference-between-two-strings/description/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:

        sumx = 0

        for i in range(0, len(s)):
            for j in range(0, len(t)):
                if s[i] == t[j]:
                    sumx += abs(i-j)

        return sumx
        
