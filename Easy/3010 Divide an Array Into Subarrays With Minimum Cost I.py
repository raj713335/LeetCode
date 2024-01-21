#  https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/


class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        s1 = nums[0]

        nums = sorted(nums[1:])

        return s1 + nums[0] + nums[1]
        
