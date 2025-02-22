# https://leetcode.com/problems/permutations/description/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
    
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])  # Store a copy of the current permutation
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # Swap back (Backtrack)
        
        backtrack(0)
        return result
        
