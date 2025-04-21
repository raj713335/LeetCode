class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)

        memo = {}

        def backtrack(i, cur_sum):

            if i == n:
                if cur_sum == target:
                    return 1
                else:
                    return 0

            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            memo[(i, cur_sum)] = backtrack(i+1, cur_sum + nums[i]) + backtrack(i+1, cur_sum - nums[i])
            return memo[(i, cur_sum)]

        return backtrack(0, 0)
