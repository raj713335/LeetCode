# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/description/


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:

        id = logs[0][0]
        longest_time = logs[0][1]


        for i in range(1, len(logs)):
            time = logs[i][1]- logs[i-1][1]
            if time > longest_time:
                longest_time = time
                id = logs[i][0]
            elif time == longest_time:
                if logs[i][0] < id:
                    id = logs[i][0]

        return id
