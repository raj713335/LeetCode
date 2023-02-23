# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        dictx = {}

        res = []

        for i in range(0, len(nums1)):
            if nums1[i][0] not in dictx:
                dictx[nums1[i][0]] = nums1[i][1]
            else:
                dictx[nums1[i][0]] += nums1[i][1]


        for i in range(0, len(nums2)):
            if nums2[i][0] not in dictx:
                dictx[nums2[i][0]] = nums2[i][1]
            else:
                dictx[nums2[i][0]] += nums2[i][1]

        for key, value in dictx.items():
            res.append([key, value])

        res = sorted(res, key= lambda x:x[0])

        return res
