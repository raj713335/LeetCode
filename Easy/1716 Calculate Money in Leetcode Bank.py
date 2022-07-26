# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        
        savings = 0
        
        counter = 0
        
        i = 0
        
        val = 1
        
        
        
        while i<n:
            if val%7 == 0:
                savings += val+counter
                counter += 1
                i += 1
                val = 1
            else:
                savings += val+counter
                i += 1
                val += 1
            print(savings)
                
        return savings
                
                
            
        
