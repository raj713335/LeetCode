# https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        comb = []
     
        for i in range(len(nums)+1):
            comb += [list(j) for j in combinations(nums, i)]

        return comb
        
