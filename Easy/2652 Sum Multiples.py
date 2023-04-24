# https://leetcode.com/problems/sum-multiples/


class Solution:
    def sumOfMultiples(self, n: int) -> int:

        nums = [3, 5, 7, 9]

        sumx = 0

        for i in range(2, n+1):
            for j in nums:
                if i % j == 0:
                    sumx += i
                    break

        return sumx
