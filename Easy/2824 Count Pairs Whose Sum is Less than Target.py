# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        count = 0

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1

        return count
