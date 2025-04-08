# https://leetcode.com/problems/longest-increasing-subsequence/


# Bottom Up Approach

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        LIS = [1] * n

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)


# Top Down Approach 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        dp = {}

        def dfs(index, prev):

            if index == n:
                return 0

            elif index in dp:
                return dp[index]

            max_length = 0 

            for i in range(index, n):
                if nums[i] > prev:
                    max_length = max(max_length, 1 + dfs(i, nums[i]))

            dp[index] = max_length
            return dp[index]

        return dfs(0, float('-inf'))
            
        
        
