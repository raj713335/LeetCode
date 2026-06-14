# https://leetcode.com/problems/check-good-integer/


class Solution:
    def checkGoodInteger(self, n: int) -> bool:

        digitsum = 0
        squaresum = 0

        for digit in str(n):
            digitsum += int(digit)
            squaresum += int(digit) ** 2

        return squaresum - digitsum >= 50

        
