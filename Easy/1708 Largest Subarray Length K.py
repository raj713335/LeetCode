# https://leetcode.com/problems/largest-subarray-length-k/description/

class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return [max(nums)]
            
        key = max(nums[:-(k-1)])
        indi = nums.index(key)

        return nums[indi:indi+k]
        
