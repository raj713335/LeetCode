# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        diagonal_max_area = 0
        max_area = 0

        for i, j in dimensions:
            temp = (i*i + j*j)**0.5
            if temp > diagonal_max_area:
                diagonal_max_area = temp
                max_area = i * j
            elif temp == diagonal_max_area:
                max_area = max(max_area, i*j)

        return max_area
        
