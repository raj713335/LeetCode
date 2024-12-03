# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/description/


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:

        max_floor = 0

        special = [bottom] + sorted(special) + [top]

        temp = special[1] - special[0]
        if temp > max_floor:
            max_floor = temp

        temp = special[-1] - special[-2]
        if temp > max_floor:
            max_floor = temp

        for i in range(1, len(special)-2):
            temp = special[i+1] - special[i] - 1
            if temp > max_floor:
                max_floor = temp

        return max_floor
