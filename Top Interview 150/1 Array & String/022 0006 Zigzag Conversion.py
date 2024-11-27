# https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s

        i = 0
        d = 1

        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[i].append(char)

            if i == 0:
                d = 1
            if i == numRows-1:
                d = -1

            i += d

        res = ''

        for each in rows:
            res += "".join(each)

        return res

                        
