# https://leetcode.com/problems/longest-arithmetic-subsequence/description/

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        max_len = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # Either start new or extend previous sequence
                dp[i][diff] = dp[j][diff] + 1
                max_len = max(max_len, dp[i][diff])

        return max_len + 1  # add 1 for the starting element
