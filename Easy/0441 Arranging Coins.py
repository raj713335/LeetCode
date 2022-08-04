# https://leetcode.com/problems/arranging-coins/


class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        count = 0
        i = 1
        
        while n >= 0:
            n -= i
            i += 1
            count += 1
            
        if n == 0:
            return count
        else:
            return count-1
        
