# https://leetcode.com/problems/house-robber/description/
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minCost(i, memo={}):
            if i in memo:
                return memo[i]
            if i < 2:
                return cost[i]
            memo[i] = cost[i] + min(minCost(i-1, memo), minCost(i-2, memo))
            return memo[i]
        
        n = len(cost)
        return min(minCost(n-1), minCost(n-2))


# Alternative Solution 

class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxCost(i, memo={}):
            if i in memo:
                return memo[i]
            if i == 1:
                return nums[0]
            if i == 2:
                return max(nums[0], nums[1])
            memo[i] = max(maxCost(i-1, memo), nums[i-1] + maxCost(i-2, memo))
            return memo[i]
        
        n = len(nums)
        return maxCost(n)
        

