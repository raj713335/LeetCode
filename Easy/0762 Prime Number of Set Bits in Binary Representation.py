# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        count = 0
        
        for i in range(left, right+1):
            flag = True
            bits = bin(i).count("1") 
            if bits == 1:
                continue
            if bits == 2:
                count += 1
                continue
            for j in range(2, bits):
                if bits % j == 0:
                    flag = False
                    break
                    
            if flag:
                count += 1
                
        return count
        
