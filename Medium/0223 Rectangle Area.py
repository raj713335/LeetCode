# https://leetcode.com/problems/rectangle-area/


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        max_lx = max(ax1, bx1)
        min_rx = min(ax2, bx2)
        if max_lx<min_rx: #overlap
            x = min_rx-max_lx
        else:
            x = 0
            
        max_ly = max(ay1, by1)
        min_ry = min(ay2, by2)
        if max_ly<min_ry: #overlap
            y = min_ry-max_ly
        else:
            y = 0

        return (ax1-ax2)*(ay1-ay2) + (bx1-bx2)*(by1-by2) - x*y

        
