# https://leetcode.com/problems/longest-harmonious-subsequence/description/


class Solution:
    def findLHS(self, nums: List[int]) -> int:

        dictx = {}

        max_count = 0

        for i in range(0, len(nums)):
            if nums[i] not in dictx.keys():
                dictx[nums[i]] = 1
            else:
                dictx[nums[i]] += 1

        sorted_le = sorted(set(nums))

        for i in range(0, len(sorted_le)-1):
            if sorted_le[i+1] - sorted_le[i] == 1:
                temp = dictx[sorted_le[i+1]] + dictx[sorted_le[i]]
                if temp > max_count:
                    max_count = temp

        return max_count 
