# https://leetcode.com/problems/fair-candy-swap/description/


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        dif = (sum(aliceSizes) - sum(bobSizes)) / 2
        A = set(aliceSizes)
        for b in set(bobSizes):
            if dif + b in A:
                return [dif + b, b]
            
