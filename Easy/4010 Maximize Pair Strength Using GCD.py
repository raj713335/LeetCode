# https://leetcode.com/problems/maximize-pair-strength-using-gcd/description/


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:

        length = len(nums)

        max_strength = 0

        for i in range(0, length-1):
            for j in range(i+1, length):
                temp_strength = int((nums[i] * nums[j]) / (gcd(nums[i], nums[j]) ** 2))
                if temp_strength > max_strength:

                    max_strength = temp_strength

        return max_strength
        
