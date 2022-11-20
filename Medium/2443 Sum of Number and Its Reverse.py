# https://leetcode.com/problems/sum-of-number-and-its-reverse/description/


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:


        for i in range(0, num):
            if i + int(str(i)[::-1]) == num:
                return True

        if num == 0:
            return True
        return False
