# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)

        sum_a_b = a + b

        sum_a_b_bin = bin(sum_a_b)

        return sum_a_b_bin[2:]