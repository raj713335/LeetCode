# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        count = 0

        for i in range(0, len(nums)):
            if nums[i] % 3 != 0:
                count += 1

        return count

        
