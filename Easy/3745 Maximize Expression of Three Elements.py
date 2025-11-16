# https://leetcode.com/problems/maximize-expression-of-three-elements/description/

class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:

        nums = sorted(nums)

        return (nums[-1] + nums[-2]) - nums[0]
        
