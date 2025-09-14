# https://leetcode.com/problems/earliest-time-to-finish-one-task/description/

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:

        smallest_time = math.inf

        for task1, task2 in tasks:
            time = task1 + task2
            if smallest_time > time:
                smallest_time = time

        return smallest_time
        
