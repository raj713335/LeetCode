# https://leetcode.com/problems/score-of-a-string/

class Solution:
    def scoreOfString(self, s: str) -> int:

        sumx = 0

        for i in range(0, len(s)-1):
            sumx += abs(ord(s[i])-ord(s[i+1]))

        return sumx
        
