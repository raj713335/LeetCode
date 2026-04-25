# https://leetcode.com/problems/valid-digit-number/description/

class Solution:
    def validDigit(self, n: int, x: int) -> bool:

        n = str(n)
        x = str(x)

        val = len(x)

        if n[0:val] == x:
            return False

        for i in range(1, len(n)):
            if n[i:i+val] == x:
                return True

        return False
        
