# https://leetcode.com/problems/split-the-array/description/


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:

        dictx = {}

        for i in range(0, len(nums)):
            if nums[i] not in dictx.keys():
                dictx[nums[i]] = 1
            else:
                dictx[nums[i]] += 1
                if dictx[nums[i]] > 2:
                    return False
        return True
        
