# https://leetcode.com/problems/sort-array-by-absolute-value/description/

class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:

        return sorted(nums, key=lambda x: abs(x))

        
