# https://leetcode.com/problems/rotate-image/

import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        matrix[:] = np.array(matrix)
        matrix[:] = np.rot90(matrix)
        matrix[:] = np.rot90(matrix)
        matrix[:] = np.rot90(matrix).tolist()
