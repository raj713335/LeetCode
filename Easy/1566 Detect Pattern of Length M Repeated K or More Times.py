# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/description/

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        

        i = 0
        while i < len(arr)-1:
            p = arr[i:i+m]
            if p*k == arr[i:i+m*k]:
                return True
            i += 1
        return False
        
