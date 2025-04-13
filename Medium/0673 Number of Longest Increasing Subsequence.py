# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

## Tabulation Method 

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        LIS = [[1, 1] for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if LIS[j][0] + 1 > LIS[i][0]:
                        LIS[i][0] = LIS[j][0] + 1
                        LIS[i][1] = LIS[j][1]
                    elif LIS[j][0] + 1 == LIS[i][0]:
                        LIS[i][1] += LIS[j][1]

        max_LIS = 0
        count = 0

        for each in LIS:
            if each[0] > max_LIS:
                max_LIS = each[0]
                count = each[1]
            elif each[0] == max_LIS:
                count += each[1]

        return count
        
# Recursive + Memoization Method

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
