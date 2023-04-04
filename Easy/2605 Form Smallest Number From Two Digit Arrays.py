# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:

        s1 = min(nums1)
        s2 = min(nums2)

        nums2 = sorted(nums2)

        for each in nums2:
            if each in nums1:
                return each

        if s1 == s2:
            return s1
        else:
            return min(int(str(s1)+str(s2)), int(str(s2)+str(s1)))
