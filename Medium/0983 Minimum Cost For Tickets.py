# https://leetcode.com/problems/minimum-cost-for-tickets/description/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        # Amount of days we are considering (total days)
        last_day = days[-1]
        
        # dp[i] will represent the minimum cost to cover up to day i
        dp = [0] * (last_day + 1)
        
        # Set of days you are traveling
        travel_days = set(days)
        
        for day in range(1, last_day + 1):
            if day not in travel_days:
                dp[day] = dp[day - 1]
            else:
                # For each travel day, choose the minimum cost by using the 1-day, 7-day, or 30-day ticket
                dp[day] = min(dp[day - 1] + costs[0], # 1-day ticket
                              dp[max(0, day - 7)] + costs[1], # 7-day ticket
                              dp[max(0, day - 30)] + costs[2]) # 30-day ticket

        return dp[last_day]
        
