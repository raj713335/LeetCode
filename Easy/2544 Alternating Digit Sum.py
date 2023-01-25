# https://leetcode.com/problems/alternating-digit-sum/description/


class Solution:

    def alternateDigitSum(self, n: int) -> int:

        i = 0

        sumx = 0

        for digit in str(n):

            if i % 2 == 0:

                sumx += int(digit)

            else:

                sumx -= int(digit)

            i += 1

        return sumx
