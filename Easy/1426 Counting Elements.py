# https://leetcode.com/problems/counting-elements/description/

class Solution:
    def countElements(self, arr: List[int]) -> int:

        unique = set(arr)
        
        count = 0
        for i in range(len(arr)):
            if arr[i]+1 in unique:
                 count += 1
        
        return count
