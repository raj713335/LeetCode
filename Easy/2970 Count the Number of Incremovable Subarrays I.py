# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/description/

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:

        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                l = nums[:i]+ nums[j:]
                if l==sorted(l) and len(l)==len(set(l)):
                    count+=1
        return count
        
