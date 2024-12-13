# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points = sorted(points, key=lambda x: x[1])

        i = 0
        count = 0

        while i < len(points):
            start = points[i]

            while i + 1 < len(points) and start[1] >= points[i+1][0]:
                i += 1

            count += 1
            i += 1

        return count
