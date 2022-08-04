# https://leetcode.com/problems/max-consecutive-ones/


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_count = 0
        count = 0 
        

        
        for each in nums:
            if each == 1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
                
        return max_count
        
