# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        max_count = 0
        count = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1

        return max(max_count, count)
        
