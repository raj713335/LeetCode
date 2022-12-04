# https://leetcode.com/problems/number-of-days-between-two-dates/description/

from datetime import datetime as dt

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs((dt.strptime(date1, "%Y-%m-%d") - dt.strptime(date2, "%Y-%m-%d")).days)
        
