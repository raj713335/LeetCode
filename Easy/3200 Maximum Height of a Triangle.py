# https://leetcode.com/problems/maximum-height-of-a-triangle/description/

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        if red < blue:
            return self.maxHeightOfTriangle(blue, red)

        h1, h2 = isqrt(blue*4+1), isqrt(blue)*2
        
        if (h1+1)**2//4 <= red:     
            return h1

        if ((h2+1)**2-1)//4 <= red: 
            return h2

        if (h1-1)**2//4 <= red:     
            return h1-1

        return h2-1
        
