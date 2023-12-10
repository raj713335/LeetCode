# https://leetcode.com/problems/find-common-elements-between-two-arrays/description/

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:


        count1 = 0
        count2 = 0

        dictx1 = {}
        dictx2 = {}

        for each in nums1:
            dictx1[each] = 1

        for each in nums2:
            dictx2[each] = 1

        for each in nums1:
            if each in dictx2.keys():
                count1 += 1

        for each in nums2:
            if each in dictx1.keys():
                count2 += 1


        return [count1, count2]
        
        
