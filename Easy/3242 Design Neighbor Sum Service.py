# https://leetcode.com/problems/design-neighbor-sum-service/description/


class neighborSum:

    def valid(self, r, c):
        if r >= 0 and r < len(self.grid) and c >= 0 and c < len(self.grid[0]):
            return True
        else:
            return False  

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        
    def adjacentSum(self, value: int) -> int:

        sumx = 0 

        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[0])):
                if self.grid[i][j] == value:

                    if self.valid(i-1, j):
                        sumx += self.grid[i-1][j]

                    if self.valid(i, j-1):
                        sumx += self.grid[i][j-1]

                    if self.valid(i+1, j):
                        sumx += self.grid[i+1][j]

                    if self.valid(i, j+1):
                        sumx += self.grid[i][j+1]

                    return sumx
            

    def diagonalSum(self, value: int) -> int:
        sumx = 0 

        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[0])):
                if self.grid[i][j] == value:

                    if self.valid(i-1, j-1):
                        sumx += self.grid[i-1][j-1]

                    if self.valid(i+1, j-1):
                        sumx += self.grid[i+1][j-1]

                    if self.valid(i-1, j+1):
                        sumx += self.grid[i-1][j+1]

                    if self.valid(i+1, j+1):
                        sumx += self.grid[i+1][j+1]

                    return sumx
        

# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
