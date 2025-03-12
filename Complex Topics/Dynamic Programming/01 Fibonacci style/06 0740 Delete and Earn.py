# https://leetcode.com/problems/delete-and-earn/description/


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        dictx = {}

        for each in nums:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1

        nums = sorted(dictx.keys())

        n = len(nums)

        if n == 0:
            return 0
        elif n == 1:
            return nums[0] * dictx[nums[0]]
        elif n == 2:
            if nums[1] == nums[0] + 1: 
                return max(nums[0] * dictx[nums[0]], nums[1] * dictx[nums[1]])
            else:
                return  (nums[0] * dictx[nums[0]] + nums[1] * dictx[nums[1]])

        dp = [0] * n

        dp[0] =  nums[0] * dictx[nums[0]]

        if nums[1] == nums[0] + 1: 
            dp[1] = max(nums[0] * dictx[nums[0]], nums[1] * dictx[nums[1]])
        else:
            dp[1] = (nums[0] * dictx[nums[0]] + nums[1] * dictx[nums[1]])

        for i in range(2, n):
            if nums[i] == nums[i-1] + 1: 
                dp[i] = max(dp[i-1], dp[i-2] + nums[i] * dictx[nums[i]])
            else:
                dp[i] = dp[i-1] + nums[i] * dictx[nums[i]]


        return dp[-1]
        
