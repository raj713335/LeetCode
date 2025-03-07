# https://leetcode.com/problems/construct-quad-tree/description/


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def buildNode(x1, y1, x2, y2):
            
            # Check if the grid has the same value
            first_val = grid[x1][y1]
            all_same = True

            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if grid[i][j] != first_val:
                        all_same = False
                        break
            
            if all_same:
                return Node(
                    val = first_val,
                    isLeaf = True
                )

            # If not, divide the grid into four sub-grids
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2

            return Node(
                val = True, # Arbitrary value when it's not a leaf
                isLeaf = False,
                topLeft = buildNode(x1, y1, mid_x, mid_y),
                topRight = buildNode(x1, mid_y + 1, mid_x, y2),
                bottomLeft = buildNode(mid_x + 1, y1, x2, mid_y),
                bottomRight = buildNode(mid_x + 1, mid_y + 1, x2, y2)
            )

        return buildNode(0, 0, len(grid)-1, len(grid)-1)
        
