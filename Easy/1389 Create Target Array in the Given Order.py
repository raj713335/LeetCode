# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        res = []
        
        for i in range(0, len(index)):
            res.insert(index[i], nums[i])
            
        return res
        
