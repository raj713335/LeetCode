# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/


class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles = sorted(piles)
        sumx = 0

        for i in range(len(piles)//3, len(piles), 2):
            sumx += (piles[i])

        return sumx

        
