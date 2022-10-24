# https://leetcode.com/problems/find-subarrays-with-equal-sum/


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        dictx = {}
        
        ii = 2
        
        for j in range(0, len(nums)-ii+1):
            sumx = sum(nums[j:j+ii])
            if sumx not in dictx:
                dictx[sumx] = 1
            else:
                return True
                
        
