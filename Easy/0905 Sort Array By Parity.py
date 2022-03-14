# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        res = []
        
        for each in nums:
            if each%2==0:
                res.insert(0, each)
            else:
                res.append(each)
                
        return res
        
