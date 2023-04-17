# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        dictx = {}

        for each in nums:
            if each not in dictx.keys():
                dictx[each] = 1
            else:
                dictx[each] += 1

        max_rows = max(dictx.values())

        res = [[] for i in range(0, max_rows)]

        for key, value in dictx.items():
            for i in range(0, value):
                res[i].append(key)

        return res
