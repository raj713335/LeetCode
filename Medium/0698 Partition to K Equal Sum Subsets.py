# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        target = total_sum // k
        nums.sort(reverse=True)  # Optimization: place bigger numbers first
        used = [False] * len(nums)
        
        memo = {}

        def dfs(k_remaining, curr_sum, start_index):
            if k_remaining == 0:
                return True
            if curr_sum == target:
                return dfs(k_remaining - 1, 0, 0)
            
            key = tuple(used)
            if key in memo:
                return memo[key]
            
            for i in range(start_index, len(nums)):
                if not used[i] and curr_sum + nums[i] <= target:
                    used[i] = True
                    if dfs(k_remaining, curr_sum + nums[i], i + 1):
                        memo[key] = True
                        return True
                    used[i] = False
            
            memo[key] = False
            return False
        
        return dfs(k, 0, 0)



class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        
        target_sum = nums_sum // k
        nums.sort(reverse=True)
        if nums[0] > target_sum:
            return False
        
        subset_sums = [0] * k
        
        def backtrack(index):
            if index == len(nums):
                return True
            for i in range(k):
                if subset_sums[i] + nums[index] <= target_sum:
                    subset_sums[i] += nums[index]
                    if backtrack(index+1):
                        return True
                    subset_sums[i] -= nums[index]
                if subset_sums[i] == 0:
                    break
            return False
        
        return backtrack(0)



            
