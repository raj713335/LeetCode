# https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        center = []
        start = []
        end = []
        
        for each in nums:
            if each <pivot:
                start.append(each)
            elif each > pivot:
                end.append(each)
            else:
                center.append(each)
                
        return(start+center+end)
        
