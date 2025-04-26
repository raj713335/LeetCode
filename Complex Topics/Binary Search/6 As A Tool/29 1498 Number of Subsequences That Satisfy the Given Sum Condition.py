# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l)
                l += 1
        return res % mod
        
