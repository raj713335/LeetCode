# https://leetcode.com/problems/lonely-pixel-ii/description/


class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:

        rows = {}
        cols = {}
        res = []
        frequency = defaultdict(int)

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
            frequency["".join(picture[i])] += 1
        
        for (x, y) in res:
            if frequency["".join(picture[x])] == rows[x] == cols[y] == target:
                count += 1

        return count
        
