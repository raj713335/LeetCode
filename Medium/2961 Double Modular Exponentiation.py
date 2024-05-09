# https://leetcode.com/problems/double-modular-exponentiation/description/


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:

        ans = []

        for i, (a, b, c, m) in enumerate(variables): 
            if (((a**b) % 10)**c) % m == target:
                ans.append(i)
                
        return ans 
        
