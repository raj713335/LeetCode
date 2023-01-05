# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        count = 1

        points = sorted(points, key = lambda x: x[1])


        prev = points[0]

        for i in range(1, len(points)):
            if (points[i][0] > prev[1]):
                count += 1
                prev = points[i]


        return count
