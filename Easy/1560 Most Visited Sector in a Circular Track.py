# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/description/

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

        a, b = rounds[0], rounds[-1]
        if a<=b: return [i for i in range(a, b+1)]
        return [i for i in range(1, b+1)] + [i for i in range(a, n+1)]

        
        
