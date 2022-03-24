# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        res = []
        
        def sort_first(key):
            return key[0]
        
        for i in range(0, len(mat)):
            val = mat[i].count(1)
            res.append([i,val])
            
        res = sorted(res, key = lambda x: x[1])
        
        val = []
        
        for i in range(0, k):
            val.append(res[i][0])
            
        return val
            
        
