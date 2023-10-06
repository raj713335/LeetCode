# https://leetcode.com/problems/rectangle-overlap/description/


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        width = min(rec2[2], rec1[2]) - max(rec2[0], rec1[0])
        height = min(rec2[3], rec1[3]) - max(rec2[1], rec1[1])
        return width > 0 and height > 0
        
