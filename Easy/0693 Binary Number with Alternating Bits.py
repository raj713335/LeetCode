# https://leetcode.com/problems/binary-number-with-alternating-bits/


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        n = bin(n)[2:]
        
        prev = n[0]
        
        for i in range(1, len(n)):
            if n[i] == prev:
                return False
            else:
                prev = n[i]
        
        return True
        
