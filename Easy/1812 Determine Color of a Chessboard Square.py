# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        dictx = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
        
        if dictx[coordinates[0]]%2==0:
            if int(coordinates[1])%2!=0:
                return True
        elif dictx[coordinates[0]]%2!=0:
            if int(coordinates[1])%2==0:
                return True
        else:
            return False
            
        
