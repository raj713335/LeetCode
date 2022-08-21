# https://leetcode.com/problems/complement-of-base-10-integer/


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        n = bin(n)[2:][::-1]
        

        sumx = 0
        for i in range(0, len(n)):
            if n[i] == "0":
                sumx += (2**i)
                
        return sumx
            
        
