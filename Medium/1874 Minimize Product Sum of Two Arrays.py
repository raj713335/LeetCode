# https://leetcode.com/problems/minimize-product-sum-of-two-arrays/description/

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:

        nums1 = sorted(nums1)
        nums2 = sorted(nums2, reverse=True)

        ans = 0

        for i in range(0, len(nums1)):
            ans += nums1[i] * nums2[i]

        return ans

        
