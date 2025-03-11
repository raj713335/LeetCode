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


# Alternative Solution 


class Solution:
    def rob(self, nums: List[int]) -> int:

        count = len(nums)
        
        if count == 1:
            return nums[0]
        if count == 2:
            return max(nums[0], nums[1])
        
        memo = nums[:]
        memo[1] = max(nums[0], nums[1])

        for i in range(2, count):
            memo[i] = max(memo[i-1], memo[i] + memo[i-2])

        return memo[count-1]
        

