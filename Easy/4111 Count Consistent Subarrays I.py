# https://leetcode.com/problems/count-consistent-subarrays-i/description/


class Solution:
    def countConsistent(self, nums: list[int]) -> int:

        count = 0

        for i in range(1, len(nums)+1):
            for j in range(0, len(nums)-i+1):
                temp = nums[j:j+i]

                mini = min(temp)

                bit_and = temp[0]
                for z in range(1, len(temp)):
                    bit_and = bit_and & temp[z]

                if bit_and == mini:
                    count += 1

        return count
        
