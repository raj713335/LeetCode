# https://leetcode.com/problems/day-of-the-year/description/


class Solution:
    def dayOfYear(self, date: str) -> int:
        
        Y, M, D = map(int, date.split('-'))
        return int((datetime.datetime(Y, M, D) - datetime.datetime(Y, 1, 1)).days + 1)
        
