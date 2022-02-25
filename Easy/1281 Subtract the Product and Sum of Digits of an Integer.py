# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        product = 1
        sumx = 0
        
        n = list(str(n))
        
        for i in range(0, len(n)):
            product *= int(n[i])
            sumx += int(n[i])
            
        return product-sumx
        
