# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/description/


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        

        even_parity = 0
        odd_parity = 0
        for chip in position:
            if chip % 2 == 0:
                even_parity += 1
            else:
                odd_parity += 1
        return min(even_parity, odd_parity)
        
