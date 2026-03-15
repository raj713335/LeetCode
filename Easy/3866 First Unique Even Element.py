# https://leetcode.com/problems/first-unique-even-element/description/

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:

        dictx = {}

        for val in nums:
            if val % 2 == 0:
                if val not in dictx.keys():
                    dictx[val] = 1
                else:
                    dictx[val] += 1
        
        for key, val in dictx.items():
            if val == 1:
                return key

        return -1
