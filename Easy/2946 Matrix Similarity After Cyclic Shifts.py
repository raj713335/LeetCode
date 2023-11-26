# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description/

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for l in mat:
            n = len(l)
            for i in range(n):
                if l[i] != l[(i + k) % n]:
                    return False
        return True
        
