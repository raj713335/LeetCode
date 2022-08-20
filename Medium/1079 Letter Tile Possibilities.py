# https://leetcode.com/problems/letter-tile-possibilities/


from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        dictx = {}
        
        for i in range(1, len(tiles)+1):
            for each in list(permutations(tiles, i)):
                if each not in dictx:
                    dictx[each] = 1
                    
        return len(dictx)
        
