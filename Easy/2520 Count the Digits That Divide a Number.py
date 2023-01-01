# https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/


class Solution:
    def countDigits(self, num: int) -> int:

        count = 0

        for each in list(str(num)):
            if num % int(each) == 0:
                count += 1

        return count
