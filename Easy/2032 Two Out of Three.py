# https://leetcode.com/problems/two-out-of-three/

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        nums = list(set(nums1))+list(set(nums2))+list(set(nums3))
        
        dictx = {}
        
        for each in nums:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
        
        res = []
        
        for key, value in dictx.items():
            if value > 1:
                res.append(key)
                
        return res
        
