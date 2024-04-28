# https://leetcode.com/problems/count-numbers-with-unique-digits-ii/description/

class Solution:
    def numberCount(self, a: int, b: int) -> int:

        count = 0

        for i in range(a, b+1):
            if len(str(i)) == len(set(str(i))):
                count += 1

        return count
