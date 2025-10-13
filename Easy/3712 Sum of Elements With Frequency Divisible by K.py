# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/description/


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:

        dictx = {}

        for i in range(0, len(nums)):
            if nums[i] not in dictx.keys():
                dictx[nums[i]] = 1
            else:
                dictx[nums[i]] += 1

        sumx = 0

        for key, value in dictx.items():
            if value % k == 0:
                sumx += (value * key)

        return sumx
        
