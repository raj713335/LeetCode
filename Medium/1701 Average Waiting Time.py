# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/?envType=daily-question&envId=2024-07-05


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        n = len(customers)

        start_time = 0
        waiting_time = 0

        for i in range(0, n):
            start_time = max(start_time, customers[i][0])
            start_time += customers[i][1]
            waiting_time += start_time - customers[i][0]

        return waiting_time / n
        
