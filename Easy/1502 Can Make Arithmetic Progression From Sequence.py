# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr = sorted(arr,  reverse = True)
        
        res = []
        
        
        for i in range(0, len(arr)-1):
            res.append(arr[i]-arr[i+1])
        
        if len(set(res)) == 1:
            return True
        else:
            return False
            
        
        
