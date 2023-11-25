# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        output = []

        prefix_sum = 0
        postfix_sum = sum(nums)

        size = len(nums)

        for i in range(0, len(nums)):
            postfix_sum -= nums[i]
            temp = ((nums[i] * i) - prefix_sum ) + (  postfix_sum - (nums[i] * (size-i-1)))
            output.append(temp)
            prefix_sum += nums[i]
            
        return output
                
        
