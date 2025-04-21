# https://leetcode.com/problems/flood-fill/description/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(image, sr, sc, color, row, col, source):
            if (sr < 0 or sr >= row or sc <0 or sc >= col):
                return 
            elif image[sr][sc]!= source:
                return
            
            image[sr][sc] = color

            dfs(image, sr-1, sc, color, row, col, source)
            dfs(image, sr+1, sc, color, row, col, source)
            dfs(image, sr, sc-1, color, row, col, source)
            dfs(image, sr, sc+1, color, row, col, source)


        
        source = image[sr][sc]
        if (source== color):
            return image
        row = len(image)
        col = len(image[0])

        dfs(image, sr, sc, color, row, col, source)
        return image
        
