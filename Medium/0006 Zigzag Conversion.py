#https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        l = len(s)


        arr=["" for x in range(l)]
        row = 0
        
        for i in range(l):

            arr[row] += s[i]

            if row == numRows - 1:
                down = False

            elif row == 0:
                down = True

            if down:
                row += 1
            else:
                row -= 1

        # Print concatenation
        # of all rows
        final = ""
        for i in range(l):
            final += arr[i]
        return final
        
        
