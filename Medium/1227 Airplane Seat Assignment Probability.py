# https://leetcode.com/problems/airplane-seat-assignment-probability/


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        
        if n == 1:
            return 1
        return 0.5
        
