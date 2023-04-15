# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/description/


class Solution:
    def convertTime(self, current: str, correct: str) -> int:

        time1 = int(current[0:2])*60 + int(current[3:])
        time2 = int(correct[0:2])*60 + int(correct[3:])

        diff = abs(time1-time2)
        
        count = 0

        count += diff // 60
        diff = diff % 60

        count += diff // 15
        diff = diff % 15

        count += diff // 5
        diff = diff % 5

        count += diff 

        return count


        
