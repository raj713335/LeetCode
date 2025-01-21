# https://leetcode.com/problems/house-robber-ii/description/

class Solution:
    def rob(self, nums: List[int]) -> int:

        def robber(nums):
            
            count = len(nums)

            if count == 1:
                return nums[0]
            if count == 2:
                return max(nums[0], nums[1])

            memo = nums[:]
            memo[1] = max(nums[0], nums[1])

            for i in range(2, count):
                memo[i] = max(memo[i-1], memo[i] + memo[i-2])

            return memo[count-1]

        if len(nums) == 1:
            return nums[0]

        return max(robber(nums[:-1]), robber(nums[1:]))
        
