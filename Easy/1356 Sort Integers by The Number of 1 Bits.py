# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        output = []
        
        arr = sorted(arr)
        
        for i in range(0, len(arr)):
            arr[i] = [arr[i], bin(arr[i]).count("1")]
            
        arr = sorted(arr, key = lambda x : x[1])
        
        for each in arr:
            output.append(each[0])
            
        return output
        
