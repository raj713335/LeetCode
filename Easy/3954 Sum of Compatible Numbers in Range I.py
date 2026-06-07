# https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/description/


class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:

        count = 0

        for i in range(max(n-k, 1), n+k+1):
            if abs(n-i) <= k and n & i == 0:
                count += i

        return count
        
