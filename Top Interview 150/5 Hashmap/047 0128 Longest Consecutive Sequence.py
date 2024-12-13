# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0

        nums = set(nums)

        for each in nums:
            if (each - 1) not in nums:
                lengthx = 0
                while (each + lengthx) in nums:
                    lengthx += 1
                longest = max(longest, lengthx)

        return longest

            
                    
        
