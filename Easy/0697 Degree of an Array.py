# https://leetcode.com/problems/degree-of-an-array/description/


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        dictx = {}

        for each in nums:
            if each not in dictx.keys():
                dictx[each] = 1
            else:
                dictx[each] += 1

        max_val = max(dictx.values())

        keys = []

        for key, val in dictx.items():
            if val == max_val:
                keys.append(key)

        min_index = math.inf
        for key in keys:
            index = []
            for i in range(0, len(nums)):
                if nums[i] == key:
                    index.append(i)
            temp = max(index)-min(index) 
            if temp < min_index:
                min_index = temp

        return min_index+1
        
