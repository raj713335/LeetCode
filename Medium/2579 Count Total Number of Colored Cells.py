# https://leetcode.com/problems/count-total-number-of-colored-cells/description/

class Solution:
    def coloredCells(self, n: int) -> int:
        return 2*n*(n-1)+1
        
