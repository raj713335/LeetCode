# https://leetcode.com/problems/combination-sum-iv/description/


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        n = len(nums)
        dp = {}

        def dfs(rem):
            if rem == 0:
                return 1
            elif rem < 0:
                return 0
            elif rem in dp:
                return dp[rem]

            ways = 0

            for num in nums:
                ways += dfs(rem-num)

            dp[rem] = ways
            return dp[rem]

        return dfs(target)   
