# # https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        for i in range(0, len(nums)):
            sumx = 0
            for each in str(nums[i]):
                sumx += int(each)
            nums[i] = sumx
            
        return min(nums)
        
