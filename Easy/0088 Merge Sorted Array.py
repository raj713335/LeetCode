# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[:] = nums1[:len(nums1)-len(nums2)] + nums2[:]
        
        nums1[:] = sorted(nums1)
        

        
