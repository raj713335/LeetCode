# https://leetcode.com/problems/lonely-pixel-i/description/


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        rows = {}
        cols = {}
        res = []

        count = 0

        for i in range(0, len(picture)):
            for j in range(0, len(picture[0])):
                if picture[i][j] == "B":
                    res.append([i, j])
                    if i not in rows:
                        rows[i] = 1
                    else:
                        rows[i] += 1
                    if j not in cols:
                        cols[j] = 1
                    else:
                        cols[j] += 1
        
        for (x, y) in res:
            if rows[x] == 1 and cols[y] == 1:
                count += 1

        return count
        
