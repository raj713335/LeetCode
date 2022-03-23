# https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        leftsum = 0
        rightsum = sum(nums)
        
        for i in range(0, len(nums)):
            if leftsum == rightsum - nums[i]:
                return i
            leftsum += nums[i]
            rightsum -= nums[i]
            
        return -1
        
