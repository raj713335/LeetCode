# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        min_dist = math.inf
        index = -1

        for i in range(0, len(points)):
            if points[i][0] == x or points[i][1] == y:
                dist = abs(x-points[i][0]) + abs(y-points[i][1])
                if dist < min_dist:
                    min_dist = dist
                    index = i 

        return index
