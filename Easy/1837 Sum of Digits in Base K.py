# https://leetcode.com/problems/sum-of-digits-in-base-k/

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        rem = n
        value = ""
        sumx = 0
        
        while n > 0:
            rem = n%k
            value += str(rem)
            n = n//k
            

        for each in value:
            sumx += int(each)
            
        return sumx
            
            
            
        
