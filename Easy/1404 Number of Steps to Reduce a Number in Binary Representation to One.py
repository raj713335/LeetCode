# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/


class Solution:
    def numSteps(self, s: str) -> int:

        s = int(s, 2)
        count = 0

        while s != 1:
            if s % 2 == 0:
                s = s//2
            else:
                s += 1
            count += 1

        return count
        
