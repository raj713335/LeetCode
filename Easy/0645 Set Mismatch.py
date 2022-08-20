# https://leetcode.com/problems/set-mismatch/


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        nums = sorted(nums)
        
        repeat = 0
        value = 0
        flagx = True
        flagy = True
        prev = 0
        counter = 1
        
        for i in range(0, len(nums)):
            
            if prev == nums[i]:
                if flagy:
                    repeat = nums[i]
                    flagy = False
                    if flagx:
                        counter -= 1
            if counter != nums[i]:
                if flagx:
                    value = counter
                    flagx = False
                    
                    
            prev = nums[i]
            counter += 1
        
        if value == 0:
            value = len(nums)
            
        
            
        return [repeat, value]
                
            
        
