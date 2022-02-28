# https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        res = [0]*n
        
        res[0] = start
        
        for i in range(1, len(res)):
            res[i] = start + 2*i
            
        rex = res[0]
        
        for each in res[1:]:
            rex ^= each
            
        return rex
        
        
