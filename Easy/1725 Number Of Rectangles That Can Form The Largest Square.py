# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/description/

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        for i in range(len(rectangles)):
            rectangles[i].remove(max(rectangles[i]))
            
        return rectangles.count(max(rectangles))
        
