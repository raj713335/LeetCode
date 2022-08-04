# https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution:
    def countSegments(self, s: str) -> int:
        
        ret = s.split(" ")
        ans = 0
        for word in ret:
            if word != "":
                ans += 1
        return ans
        
