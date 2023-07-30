# https://leetcode.com/problems/number-of-employees-who-met-the-target/description/

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:

        count = 0

        for each in hours:
            if each >= target:
                count += 1

        return count
