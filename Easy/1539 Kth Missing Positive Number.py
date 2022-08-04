# https://leetcode.com/problems/kth-missing-positive-number/


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        output = []
        
        i = 1
        ii = 1
        length = len(arr)
        
        while k > 0: 
            if (length < i) or (ii != arr[i-1]):
                k-=1
                output.append(ii)
            else:
                i+=1
            ii+=1

                
        return output[-1]
            
        
