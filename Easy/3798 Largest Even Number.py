# https://leetcode.com/problems/largest-even-number/description/

class Solution:
    def largestEven(self, s: str) -> str:

        s = str(s)

        while s != "":
            if int(s) % 2 == 0:
                return s
            else:
                s = str(s[:-1])

        return ""

        
