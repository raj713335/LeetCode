# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        
        for i in range(0, n+1):
            res.append(bin(i).count('1'))
            
        return res
        
