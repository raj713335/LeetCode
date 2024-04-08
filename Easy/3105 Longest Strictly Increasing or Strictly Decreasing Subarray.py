# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        last = nums[0]
        count = 1
        max_count = 0
        up = False
        down = False
        for i in range(1, len(nums)):
            if nums[i] > last:
                if down:
                    if count > max_count:
                        max_count = count
                    down = False
                    count = 1
                count += 1
                up = True
                last = nums[i]
            elif nums[i] < last:
                if up:
                    if count > max_count:
                        max_count = count
                    up = False
                    count = 1
                count += 1
                down = True
                last = nums[i]
            else:
                if count > max_count:
                    max_count = count
                up = False
                down = False
                count = 1
                last = nums[i]

        return max(count, max_count)

        
