# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        length = len(nums)
        maxi = -math.inf
        for i in range(0, (length//2)):
            temp = nums[i]+nums[length-i-1]
            if temp > maxi:
                maxi = temp
                
        return maxi
        
