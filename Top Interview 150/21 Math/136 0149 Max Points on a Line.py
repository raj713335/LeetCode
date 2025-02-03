# https://leetcode.com/problems/max-points-on-a-line/description/

from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        def findline(x0,yo,x1,y1):
            if y0 == y1:
                return 0, y0
            if x0 == x1:
                return x0, None
            else:
                slope = (y1-y0)/(x1-x0)
                intercept = y0 - slope * x0
                return slope, intercept

        
        if len(points) == 1:
            return 1
        lines = defaultdict(lambda: set())
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x0, y0 = points[i]
                x1, y1 = points[j]
                line = findline(x0, y0, x1, y1)
                lines[line].add(i)
                lines[line].add(j)

        return max([len(lines[line]) for line in lines])
