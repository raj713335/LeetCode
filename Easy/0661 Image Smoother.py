# https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        results = []
        rows = len(img)
        cols = len(img[0])

        for i in range(0, rows):
            temp = []
            for j in range(0, cols):
                count = 0
                s = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if 0 <= i + dx < rows and 0 <= j+dy < cols:
                            s += img[i+dx][j+dy]
                            count += 1
                temp.append(s//count)
            results.append(temp)

        return results
        
