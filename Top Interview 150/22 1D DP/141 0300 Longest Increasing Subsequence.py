# https://leetcode.com/problems/longest-increasing-subsequence/description/

# Time Complexity: O(n^2) (where n is the length of the input list `nums`, due to memoization over (index, prev) pairs and looping from index to n)
# Space Complexity: O(n^2) (due to the memoization dictionary and the recursion stack)


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

      
