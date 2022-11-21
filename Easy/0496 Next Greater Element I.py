# https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        output = []

        for each in nums1:
            index = nums2.index(each)
            val = -1
            for i in range(index+1, len(nums2)):
                if nums2[i] > each:
                    val = nums2[i]
                    break
            output.append(val)

        return output
        
