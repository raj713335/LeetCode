# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        arr = nums
        n = len(arr)
        memo = {}

        def dfs(i, remaining):
            # Base case: if we reach sum = 0
            if remaining == 0:
                return 1
            if i == n or remaining < 0:
                return 0

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            # Option 1: pick current element (stay at same index since repetition is allowed)
            pick = dfs(i, remaining - arr[i])

            # Option 2: skip current element and move to next
            skip = dfs(i + 1, remaining)

            memo[(i, remaining)] = pick + skip
            return memo[(i, remaining)]

        return dfs(0, target)
