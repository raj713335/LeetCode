# https://leetcode.com/problems/minimum-operations-to-equalize-array/description/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = nums.count(nums[0])
        return 1 if cnt < len(nums) else 0
        
