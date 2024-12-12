# https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = {}
        
        while True:
            
            sumx = 0

            for each in str(n):
                sumx += (int(each) ** 2)

            if sumx == 1:
                return True
            if sumx not in seen:
                seen[sumx] = 1
            else:
                return False

            n = sumx
        
