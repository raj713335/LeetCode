# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        
        n = str(n)
        seen = set()
        
        while True:
            
            
            sumx = 0
            
            for each in n:
                sumx += (int(each)**2)
            
            n = str(sumx)
          
        
            if int(n) == 1:
                return True
            if int(n) not in seen:
                seen.add(int(n))
            else:
                return False
                
        
