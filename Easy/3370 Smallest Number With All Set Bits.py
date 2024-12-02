# https://leetcode.com/problems/smallest-number-with-all-set-bits/description//


class Solution:
    def smallestNumber(self, n: int) -> int:

        for i in range(n, 10000):
            temp = set(list(bin(i)[2:]))
            if len(temp) == 1 and temp == {'1'}:
                return i
