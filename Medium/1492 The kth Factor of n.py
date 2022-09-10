# https://leetcode.com/problems/the-kth-factor-of-n/


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        count = k-1
        if count == 0:
            return 1
        
        for i in range(2, int(n//2)+1):
            if n % i == 0:
                count -= 1
                if count == 0:
                    return i
        if count == 1:
            return n
        return -1
        
