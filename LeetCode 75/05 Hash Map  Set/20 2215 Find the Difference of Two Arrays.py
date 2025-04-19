# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        dictx1 = {}
        dictx2 = {}
        
        output = [[], []]
        
        for each in set(nums1):
            dictx1[each] = 1
            
        for each in set(nums2):
            dictx2[each] = 1
            
        for key, val in dictx1.items():
            if key not in dictx2:
                output[0].append(key)
                
        for key, val in dictx2.items():
            if key not in dictx1:
                output[1].append(key)
                
        return output