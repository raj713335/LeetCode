# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = {}  # (index) -> (length, count)

        def dfs(i):
            if i in dp:
                return dp[i]

            max_len = 1
            count = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    length_j, count_j = dfs(j)
                    if length_j + 1 > max_len:
                        max_len = length_j + 1
                        count = count_j
                    elif length_j + 1 == max_len:
                        count += count_j

            dp[i] = (max_len, count)
            return dp[i]

        max_length = 0
        total_count = 0

        for i in range(n):
            length, count = dfs(i)
            if length > max_length:
                max_length = length
                total_count = count
            elif length == max_length:
                total_count += count

        return total_count
