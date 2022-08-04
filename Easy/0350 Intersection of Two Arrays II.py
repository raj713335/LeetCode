# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dictx = {}
        output = []
        
        for each in nums1:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
                
        for each in nums2:
            if each not in dictx:
                continue
            elif dictx[each] < 1:
                continue
            else:
                output.append(each)
                dictx[each] -=1
            
        return output
        
