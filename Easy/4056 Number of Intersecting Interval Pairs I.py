# https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/description/


class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:

        count = 0

        for i in range(0, len(intervals)-1):
            for j in range(i+1, len(intervals)):
                if (intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][0]) or (intervals[i][1] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]) or (intervals[i][0] <= intervals[j][1] and intervals[i][1] >= intervals[j][1]):
                    count += 1

        return count
        
