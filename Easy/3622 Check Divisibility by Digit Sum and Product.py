# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/description/

class Solution:
    def checkDivisibility(self, n: int) -> bool:

        sumx = 0
        product = 1

        n_array = list(str(n))

        for i in range(0, len(n_array)):
            sumx += int(n_array[i])
            product *= int(n_array[i])

        return True if int(n) % (sumx + product) == 0 else False
        
