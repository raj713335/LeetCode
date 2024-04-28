# https://leetcode.com/problems/two-sum-less-than-k/description/

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        maxi = -1

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                temp = nums[i] + nums[j]

                if temp < k:
                    if temp > maxi:
                        maxi = temp

        return maxi
        
