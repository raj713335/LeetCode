# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        res = 0
        
        step = 1
        
        while step <= len(arr):
            for i in range(0, len(arr)-step+1):
                #print(arr[i:i + step])
                res += sum(arr[i:i + step])

            step += 2
            
        return res
            
        
