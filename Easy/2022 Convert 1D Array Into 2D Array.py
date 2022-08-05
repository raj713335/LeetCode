# https://leetcode.com/problems/convert-1d-array-into-2d-array/


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        output = []
        
        if m*n != len(original):
            return output
        
        for i in range(0, len(original), n):
            output.append(original[i:i+n])
            
        return output
            
        
