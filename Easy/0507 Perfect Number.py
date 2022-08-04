# https://leetcode.com/problems/perfect-number/


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        sumx = 1
        
        if num == 1:
            return False
        
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                sumx += (num//i)+i
                
        return sumx == num
        
