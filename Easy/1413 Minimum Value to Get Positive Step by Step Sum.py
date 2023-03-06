# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/


class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]

        temp=min(nums)
        if temp>0:
            return 1
        else:
            return -temp+1
        
