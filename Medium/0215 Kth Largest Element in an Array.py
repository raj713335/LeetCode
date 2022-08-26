# https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        return sorted(nums)[-k]
        
