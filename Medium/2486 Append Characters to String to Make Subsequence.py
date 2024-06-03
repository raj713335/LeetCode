# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        j = 0

        for i in range(0, len(s)):
            try:
                if s[i] == t[j]:
                    j += 1
            except:
                return 0

        return len(t)-j
        
