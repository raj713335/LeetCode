# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/description/


class Solution:
    def countElements(self, nums: List[int]) -> int:

        # nums = sorted(nums)

        mini = nums.count(min(nums))
        mixi = nums.count(max(nums))

        if len(nums) < 3:
            return 0

        if min(nums) == max(nums):
            return 0

        return len(nums)-mini-mixi


        
