# https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/


class Solution:
    def minimumFlips(self, n: int) -> int:

        n = bin(n)[2:]

        n_rev = n[::-1]

        count = 0

        for i in range(0, len(n)):
            if n[i] != n_rev[i]:
                count += 1

        return count
        
