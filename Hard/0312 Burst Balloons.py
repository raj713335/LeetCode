# https://leetcode.com/problems/burst-balloons/description/

class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]

        n = len(nums)

        dp = {}

        def mcm(arr, i, j):

            if i + 1 == j:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]
        
            min_cost = float("-inf")

            for k in range(i + 1, j):
                min_cost = max(min_cost, mcm(arr, i, k) + mcm(arr, k, j) + arr[i] * arr[k]* arr[j])

            dp[(i, j)] = min_cost
            return dp[(i, j)]

        return mcm(nums, 0, n-1)    

        
