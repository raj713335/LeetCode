# https://leetcode.com/problems/day-of-the-week/description/


import datetime, calendar

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return calendar.day_name[datetime.date(year, month, day).weekday()]
        
