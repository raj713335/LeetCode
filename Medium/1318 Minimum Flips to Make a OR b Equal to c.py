# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        flips = 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            c_bit = (c >> i) & 1

            if c_bit == 0:
                flips += a_bit + b_bit  # flip any 1s in a or b to 0
            else:
                if a_bit == 0 and b_bit == 0:
                    flips += 1  # need at least one 1 to match c_bit == 1
        return flips
        
