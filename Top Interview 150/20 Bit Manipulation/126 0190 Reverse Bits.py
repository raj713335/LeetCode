# https://leetcode.com/problems/reverse-bits/description/

class Solution:
    def reverseBits(self, n: int) -> int:

        n = list(str(bin(n)[2:]))

        len_n = len(n)

        n = ['0'] * (32-len_n) + n

        res = 0

        for i in range(0, 32):
            res += int(n[i]) * (2 ** i)

        return res
