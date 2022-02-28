# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        previous = -101
        count = 0        
        for i in range(len(nums)):
            if nums[i]!=previous:
                previous = nums[i]
                count+=1
                nums[count-1] =nums[i]
        return count
        
