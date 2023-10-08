# https://leetcode.com/problems/count-days-spent-together/description/

from datetime import datetime

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        start , end = max(arriveAlice, arriveBob), min(leaveAlice, leaveBob)
        if start > end: 
            return 0
        x = datetime.strptime(start, '%m-%d')
        y = datetime.strptime(end, '%m-%d')
        return abs((y - x).days)  + 1

        
