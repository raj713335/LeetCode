# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxi = -1
        
        for i in range(len(arr)-1, -1, -1):
            arr[i], maxi = maxi, max(maxi,arr[i])
            
        return arr
        
