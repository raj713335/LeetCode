# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/


from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        total_distinct = len(set(nums))
        freq = defaultdict(int)
        left = 0
        distinct = 0
        result = 0

        for right in range(n):
            if freq[nums[right]] == 0:
                distinct += 1
            freq[nums[right]] += 1

            while distinct == total_distinct:
                # Every subarray starting from left to right is complete
                result += n - right  # All subarrays ending at right or beyond
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct -= 1
                left += 1

        return result
                
