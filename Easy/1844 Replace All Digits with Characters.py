# https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution:
    def replaceDigits(self, s: str) -> str:
        
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

        res = ""

        for i in range(0, len(s)-1, 2):
            res += s[i]
            res += chars[chars.index(s[i])+int(s[i+1])]

        if len(s) % 2 == 0:
            return res
        else:
            return res+s[-1]
