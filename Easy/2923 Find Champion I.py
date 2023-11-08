# https://leetcode.com/problems/find-champion-i/description/

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:

        count = len(grid[0]) - 1

        for i in range(0, len(grid)):
            if grid[i].count(1) == count:
                return i
        
