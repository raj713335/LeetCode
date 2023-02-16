# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr = sorted(arr)

        dictx = {}

        for i in range(0, len(arr)-1):

            temp = arr[i+1]-arr[i]

            if temp not in dictx:

                dictx[temp] = [[arr[i], arr[i+1]]]

            else:

                dictx[temp].append([arr[i], arr[i+1]])

        key = min(list(dictx.keys()))

        return dictx[key]
