# https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/description/

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:

        count = 0 
        sortedx = sorted(nums)
        temp = nums

        for i in range(0, len(nums)):
            if temp == sortedx:
                return count
            else:
                temp = [nums[-1]] + nums[:-1]
                count += 1
                nums = temp

        return -1        
