# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/


import math

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        min_color = math.inf

        for i in range(0, len(blocks)-k+1):
            temp = blocks[i:i+k].count("W")
            if min_color > temp:
                min_color = temp

        return min_color
