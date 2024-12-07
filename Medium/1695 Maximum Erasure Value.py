# https://leetcode.com/problems/maximum-erasure-value/description/


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        j = 0

        max_sum = 0
        sumx = 0
        dictx = {}

        for i in range(0, len(nums)):
            sumx += nums[i] 
            while nums[i] in dictx.keys():
                del dictx[nums[j]]
                sumx -= nums[j]
                j += 1

            max_sum = max(max_sum, sumx)
            dictx[nums[i]] = 1

        return max_sum
        
