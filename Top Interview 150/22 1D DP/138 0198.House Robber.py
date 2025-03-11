# https://leetcode.com/problems/house-robber/description/

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
        

