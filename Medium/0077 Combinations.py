# https://leetcode.com/problems/combinations/


from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        value  = [i for i in range(1,n+1)]

        
        combination = list(map(list,combinations(value, k)))
        
        return combination
