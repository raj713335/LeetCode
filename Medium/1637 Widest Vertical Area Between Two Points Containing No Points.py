# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/?envType=daily-question&envId=2023-12-21


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        max_distance = 0
        points = sorted(points)

        for i in range(1, len(points)):
            temp = points[i][0] - points[i-1][0]
            max_distance = max(max_distance, temp)
        
        return max_distance
        
