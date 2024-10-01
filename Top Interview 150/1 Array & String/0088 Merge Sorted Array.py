# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[:] = sorted(nums1[:m] + nums2[:n])

        return nums1

        
