# https://leetcode.com/problems/number-of-valid-subarrays/description/


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:

        length = len(nums)

        count = length

        for i in range(0, length):
            j = i + 1
            prev = nums[i]
            while j < length:
                if prev <= nums[j]:
                    count += 1
                    j += 1
                else:
                    break

        return count
        
