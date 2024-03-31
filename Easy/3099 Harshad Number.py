# https://leetcode.com/problems/harshad-number/description/

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:

        div = 0

        for each in str(x):
            div += int(each)

        if x % div == 0:
            return div
        else:
            return -1
