# https://leetcode.com/problems/maximum-product-of-two-digits/description/

class Solution:
    def maxProduct(self, n: int) -> int:

        n = list(str(n))
        n = list(map(int, n))
        n = sorted(n)

        return n[-1] * n[-2]
        
