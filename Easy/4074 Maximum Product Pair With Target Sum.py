# https://leetcode.com/problems/maximum-product-pair-with-target-sum/description/


class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:

        max = -math.inf
        max_pair = [-1, -1]

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    temp_prod = nums[i] * nums[j]
                    if temp_prod > max:
                        if nums[i] > nums[j]:
                            max_pair = [i, j]
                            max = temp_prod
                        elif nums[j] > nums[i]:
                            max_pair = [j, i]
                            max = temp_prod

        return max_pair
        
