# https://leetcode.com/problems/number-of-even-and-odd-bits/description/


class Solution:
    def evenOddBit(self, n: int) -> List[int]:

        n = bin(n)[2:][::-1]
        odd = 0
        even = 0

        for i in range(0, len(n)):
            if i % 2 == 0:
                if n[i] == "1":
                    even += 1
                    continue
            if i % 2 != 0:
                if n[i] == "1":
                    odd += 1

        return [even,odd]
