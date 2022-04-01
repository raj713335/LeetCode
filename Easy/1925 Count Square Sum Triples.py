# https://leetcode.com/problems/count-square-sum-triples/

class Solution:
    def countTriples(self, n: int) -> int:
        
        count = 0
        
        dictx = {}
        
        for i in range(1,n+1):
            dictx[i*i] = 1
            
            
        for i in range(1, n+1):
            for j in range(1, n+1):
                if (i*i+j*j) in dictx:
                    count += 1
                    
        return count
        
