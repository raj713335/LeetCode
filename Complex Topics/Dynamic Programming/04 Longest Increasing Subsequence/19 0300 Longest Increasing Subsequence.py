# https://leetcode.com/problems/longest-increasing-subsequence/description/

# Time Complexity: O(n^2) (where n is the length of the input list `nums`, due to memoization over (index, prev) pairs and looping from index to n)
# Space Complexity: O(n^2) (due to the memoization dictionary and the recursion stack)


# Approach : Patience Sorting + Binary Search (O(n log n))

import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        sub = []
        for num in nums:
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)
            
        


# Recursive + Memoization Approach 

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


# Bottom-Up Approach

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        LIS = [1] * (n)

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
        
        