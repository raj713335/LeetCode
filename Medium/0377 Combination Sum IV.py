# https://leetcode.com/problems/combination-sum-iv/description/


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}

        def backtrack(remaining):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            if remaining in memo:
                return memo[remaining]
            
            count = 0
            for num in nums:
                count += backtrack(remaining - num)
            
            memo[remaining] = count
            return count

        return backtrack(target)
