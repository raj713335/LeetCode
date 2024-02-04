# https://leetcode.com/problems/ant-on-the-boundary/description/

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:

        count = 0
        step = 0

        for i in range(0, len(nums)):
            step += nums[i]
            if step == 0:
                count += 1
           
        return count      
