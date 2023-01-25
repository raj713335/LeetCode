# https://leetcode.com/problems/minimum-common-value/description/

class Solution:

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        dictx = {}

        for each in nums2:

            dictx[each] = 1

        for each in nums1:

            if each in dictx:

                return each

        return -1
