# https://leetcode.com/problems/trim-trailing-vowels/description/

class Solution:
    def trimTrailingVowels(self, s: str) -> str:

        s = list(s)[::-1]

        for i in range(0, len(s)):
            if s[i] in ["a", "e", "i", "o", "u"]:
                s[i] = ""
                continue
            else:
                break

        return "".join(s[::-1])
        
