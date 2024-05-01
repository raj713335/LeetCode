# https://leetcode.com/problems/convert-to-base-2/description/

class Solution:
    def baseNeg2(self, n: int) -> str:
        
        if n == 0: return "0"
        ans = ""
        while n != 0:
            ans = str(n % 2) + ans 
            n = (n - 1) // -2 
        return ans
