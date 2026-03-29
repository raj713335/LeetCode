# https://leetcode.com/problems/first-matching-character-from-both-ends/description/


class Solution:
    def firstMatchingIndex(self, s: str) -> int:

        index = -1
        n = len(s)

        for i in range(0, n):
            if s[i] == s[n - i - 1]:
                return i

        return index
        
