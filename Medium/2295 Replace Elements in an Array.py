# https://leetcode.com/problems/replace-elements-in-an-array/description/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        dictx = {}

        for i in range(0, len(nums)):
            dictx[nums[i]] = i

        for key, value in operations:
            index = dictx[key]
            nums[index] = value
            del dictx[key]
            dictx[value] = index
        
        return nums
