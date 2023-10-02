# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        max_value = 0

        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    temp = ((nums[i]-nums[j]) * nums[k])
                    if temp > max_value:
                        max_value = temp

        return max_value

        
