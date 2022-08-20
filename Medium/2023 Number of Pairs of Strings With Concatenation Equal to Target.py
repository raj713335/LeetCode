# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        count = 0
        
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    if nums[i]+nums[j] == target:
                        count += 1
                        
        return count
        
