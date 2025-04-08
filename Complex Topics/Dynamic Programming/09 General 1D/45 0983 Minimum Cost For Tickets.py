# https://leetcode.com/problems/minimum-cost-for-tickets/description/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        n = len(days)
        last_day = days[-1]

        dp = {}

        def dfs(index):

            if index >= n:
                return 0

            if index in dp:
                return dp[index]

            day = days[index]

            day_1 = costs[0] + dfs(index + 1)

            index_7 = index

            while index_7 < n and days[index_7] < day + 7:
                index_7 += 1

            day_2 = costs[1] + dfs(index_7)

            index_30 = index

            while index_30 < n and days[index_30] < day + 30:
                index_30 += 1

            day_3 = costs[2] + dfs(index_30)

            min_cost = min(day_1, day_2, day_3)
            dp[index] = min_cost

            return dp[index]


        return dfs(0)
        
