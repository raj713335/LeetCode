# https://leetcode.com/problems/maximum-strong-pair-xor-i/description/


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        maxi = 0

        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    temp = nums[i] ^ nums[j]
                    if temp > maxi:
                        maxi = temp

        return maxi
        
