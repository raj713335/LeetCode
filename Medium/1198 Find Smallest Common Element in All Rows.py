# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/description/

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        dictx = {}

        length = len(mat)

        for arr in mat:
            for i in range(0, len(arr)):
                if arr[i] not in dictx:
                    dictx[arr[i]] = 1
                else:
                    dictx[arr[i]] += 1



        for key, value in dictx.items():
            if value == length:
                return key

        return -1
