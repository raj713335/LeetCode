# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        result = 0
        windowSum = 0
        right = 0

        for left in range(n):
            while right < n and (windowSum + nums[right]) * (right - left + 1) < k:
                windowSum += nums[right]
                right += 1
            
            result += right - left            
            windowSum -= nums[left]
        
        return result 
        
