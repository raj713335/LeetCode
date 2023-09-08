# https://leetcode.com/problems/minimum-operations-to-make-array-equal/description/


class Solution:
    def minOperations(self, n: int) -> int:
        if n%2 == 1:
            return (n//2) * (n//2+1)
        else:
            return (n//2) ** 2
        
