# https://leetcode.com/problems/reverse-bits/


class Solution:
    def reverseBits(self, n: int) -> int:
        

        return(int(str('{:032b}'.format(n))[::-1],2))
        
