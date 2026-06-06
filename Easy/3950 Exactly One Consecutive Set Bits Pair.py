# https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/description/


class Solution:
    def consecutiveSetBits(self, n: int) -> bool:

        n = bin(n)[2:]

        count = 0

        for i in range(1, len(n)):
            if n[i-1] == '1' and n[i-1] == n[i]:
                count += 1
  
        if count == 1:
            return True
        else:
            return False
        
