import math

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxvol = 0
        
        left = 0
        right = len(height)-1
        
        while (left<right):
            temp = (min(height[left],height[right])*(right-left))
            if temp >maxvol:
                maxvol = temp
                
            if height[left]> height[right]:
                right -= 1
            else:
                left +=1
                
        return maxvol
                
