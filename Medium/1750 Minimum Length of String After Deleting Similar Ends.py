# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/


class Solution:
    def minimumLength(self, s: str) -> int:

        if len(s) == 1:
            return 1
        if len(set(s)) == 1:
            return 0

        i, j = 0, len(s)-1

        while i < j:
            if s[i] == s[j]:
                while s[i] == s[i+1]:
                    i += 1
                while s[j] == s[j-1]:
                    j -= 1
                i += 1
                j -= 1
            else:
                return len(s[i:j+1])

        return len(s[i:j+1])              
        
