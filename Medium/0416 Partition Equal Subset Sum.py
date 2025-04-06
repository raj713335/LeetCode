# https://leetcode.com/problems/partition-equal-subset-sum/description/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        
        sumx = sum(nums)

        if sumx % 2 != 0:
            return False

        target = sumx // 2

        ## Resursion
        # memo = {}

        # def dfs(index, curr_sum):
        #     if curr_sum == target:
        #         return True
        #     elif curr_sum > target or index >= n:
        #         return False


        #     if (index, curr_sum) in memo:
        #         return memo[(index, curr_sum)] 

        #     include = dfs(index + 1, curr_sum + nums[index])
        #     exclude = dfs(index + 1, curr_sum)

        #     memo[(index, curr_sum)] = include or exclude
        #     return memo[(index, curr_sum)]


        # return dfs(0, 0)

        ## Optimization Using 1D DP Array (Bottom-Up)

        DP = [False] * (target+1)

        DP[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                DP[i] = DP[i] or DP[i-num]

        return DP[target]
