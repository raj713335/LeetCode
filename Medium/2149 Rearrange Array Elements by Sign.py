# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positive = []
        negative = []
        
        result = []
        
        for each in nums:
            if each < 0:
                negative.append(each)
            else:
                positive.append(each)
        
        for i in range(0, len(negative)):
            result.append(positive[i])
            result.append(negative[i])
            
        return result
        
