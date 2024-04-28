# https://leetcode.com/problems/make-a-square-with-the-same-color/description/

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        for i in range(0, 2):
            for j in range(0, 2):
                w = 0
                b = 0
                
                if grid[i][j] == "B":
                    b += 1
                else:
                    w += 1
                
                if grid[i+1][j] =="B":
                    b += 1
                else:
                    w += 1

                if grid[i][j+1] == "B":
                    b += 1
                else:
                    w += 1

                if grid[i+1][j+1] =="B":
                    b += 1
                else:
                    w += 1

                if w == 1 or b == 1 or w == 4 or b == 4:
                    return True
                  
        return False

        
