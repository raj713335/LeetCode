# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        res = []

        alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                     "T", "U", "V", "W", "X", "Y", "Z"]

        start_index = alphabets.index(s[0])
        end_index = alphabets.index(s[3])

        for i in range(start_index, end_index+1):
            for j in range(int(s[1]), int(s[4])+1):
                temp = alphabets[i]+str(j)
                res.append(temp)

        return res
