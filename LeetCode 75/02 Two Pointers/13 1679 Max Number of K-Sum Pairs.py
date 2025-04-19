# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        n = len(nums)
        count = 0

        i, j = 0, n-1

        while i < j:
            temp = nums[i] + nums[j]

            if temp > k:
                j -= 1
            elif temp < k:
                i += 1
            else:
                count += 1
                i += 1
                j -= 1
        
        return count
        
