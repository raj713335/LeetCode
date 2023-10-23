# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/description/

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:

        val = []

        for i in range(0, len(nums)-1):
            if nums[i] == key:
                val.append(nums[i+1])

        dictx = {}

        for each in val:
            if each in dictx.keys():
                dictx[each] += 1
            else:
                dictx[each] = 1

        max_key = 0
        max_value = 0

        for key, val in dictx.items():
            print(key, val)
            if max_value < val:
                max_value = val
                max_key = key

        return max_key
