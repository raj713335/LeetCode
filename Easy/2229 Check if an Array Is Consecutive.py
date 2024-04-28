# https://leetcode.com/problems/check-if-an-array-is-consecutive/description/

class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        x = min(nums)

        y = x + len(nums) -1 

        nums = sorted(nums)

        index = 0
        for i in range(x, y+1):
            if i != nums[index]:
                return False
            
            index += 1

        return True
        
