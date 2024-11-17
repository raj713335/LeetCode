# https://leetcode.com/problems/make-array-elements-equal-to-zero/description/

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        valid_count = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                if sum(nums[:i]) == sum(nums[i+1:]):
                    valid_count += 2
                if abs(sum(nums[:i]) - sum(nums[i+1:])) == 1:
                    valid_count += 1

        return valid_count
                
        
