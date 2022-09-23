# https://leetcode.com/problems/largest-perimeter-triangle/


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        A = sorted(nums, reverse = True)
        
        for i in range(3,len(A)+1):
            if(A[i-3] < A[i-2] + A[i-1]):
                return sum(A[i-3:i])
        return 0
        
