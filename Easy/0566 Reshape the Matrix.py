# https://leetcode.com/problems/reshape-the-matrix/


import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        try:
            return np.reshape(mat, (r,c)).tolist()
        except:
            return mat
        
        
