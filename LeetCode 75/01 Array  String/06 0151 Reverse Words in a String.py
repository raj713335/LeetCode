# https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip().split(" ")
        res = []

        for i in range(0, len(s)):
            if s[i] != "":
                res.append(s[i])

        return " ".join(res[::-1])
        
