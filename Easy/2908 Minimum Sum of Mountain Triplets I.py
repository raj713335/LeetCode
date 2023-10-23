# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/


class Solution:
    def minimumSum(self, nums: List[int]) -> int:

        min_sum = math.inf

        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        temp = nums[i] + nums[j] + nums[k]
                        if temp < min_sum:
                            print(temp, i, j, k)
                            min_sum = temp

        if min_sum == math.inf:
            return -1
        else:
            return min_sum
        
