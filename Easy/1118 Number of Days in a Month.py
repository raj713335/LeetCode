# https://leetcode.com/problems/number-of-days-in-a-month/description/

class Solution:
    def numberOfDays(self, year: int, month: int) -> int:

        mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            mon[1] = 29
        return mon[month-1]
        
