# https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/description/

class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:

        startTime = list(map(int, startTime.split(":")))
        endTime = list(map(int, endTime.split(":")))

        def toTime(x):
            return (x[0] * 3600) + (x[1] * 60) + x[2]

        return toTime(endTime) - toTime(startTime)
        
