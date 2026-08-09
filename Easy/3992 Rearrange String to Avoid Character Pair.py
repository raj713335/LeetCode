# https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/description/

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:

        count_x = s.count(x)
        count_y = s.count(y)

        res = y * count_y

        for i in range(0, len(s)):
            if s[i] != x and s[i] != y:
                res += s[i]


        res += (x * count_x)

        return res
        
