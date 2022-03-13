# https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        res =""
        count = 0
        
        for i in range(0, len(arr)):
            if arr.count(arr[i]) == 1:
                count += 1
                if k == count:
                    return arr[i]
        return res
        
