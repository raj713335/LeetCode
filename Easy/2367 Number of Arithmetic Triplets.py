# https://leetcode.com/problems/number-of-arithmetic-triplets/


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        count = 0
        
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count += 1
                        
        return count
        
