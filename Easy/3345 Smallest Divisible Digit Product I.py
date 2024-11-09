# https://leetcode.com/problems/smallest-divisible-digit-product-i/description/


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:


        while True:
            temp = 1

            for each in str(n):
                temp *= int(each)

            if (temp) % t == 0:
                return n
            else:
                n += 1
