# https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/description/


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:

        dictx = {}

        length = len(arrays)

        for arr in arrays:
            for i in range(0, len(arr)):
                if arr[i] not in dictx:
                    dictx[arr[i]] = 1
                else:
                    dictx[arr[i]] += 1

        
        res = []

        for key, value in dictx.items():
            if value == length:
                res.append(key)

        return res
