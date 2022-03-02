# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0

        for i in range(1, len(nums)+1):
            temp = combinations(nums, i)
            for each in temp:
                tx = 0
                for jj in each:
                    tx ^= jj
                res += tx

        return res

                
        
