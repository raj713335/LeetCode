# https://leetcode.com/problems/binary-digit-score/description/

class Solution:
    def calculateScore(self, a: int, b: int) -> int:

        a = bin(a)[2:].count("1")
        b = bin(b)[2:].count("1")

        if a >= b:
            return a * b
        else:
            return b // a
