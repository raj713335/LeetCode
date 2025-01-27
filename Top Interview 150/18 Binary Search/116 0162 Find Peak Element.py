# https://leetcode.com/problems/find-peak-element/description/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
         
        while l <= r: 
            mid = (l + r)//2    
            # left neighbour greater
            if mid > 0 and nums[mid] < nums[mid - 1]:
                r = mid - 1

            # right neighbour greater
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                return mid
   
        
