# https://leetcode.com/problems/find-peak-element/description/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # return nums.index(max(nums))
        
        left, right = 0, len(nums) - 1
         
        while left < right: 
            index = (left + right)//2    
            # peak is in the left half, excluding index
            if nums[index] <= nums[index +1]:
                left = index + 1

            # peak is in the right half, including index     
            else :
                right = index 
   
        return left
        
