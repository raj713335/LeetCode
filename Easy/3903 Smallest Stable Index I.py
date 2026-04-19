# https://leetcode.com/problems/smallest-stable-index-i/description/


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        for i in range(0, len(nums)):
            maxi, mini = max(nums[:i+1]), min(nums[i:])

            if maxi - mini <= k:
                return i

        return -1
        
