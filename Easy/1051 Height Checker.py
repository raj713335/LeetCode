# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        count = 0
        
        hig = sorted(heights)
        
        for i in range(0, len(heights)):
            if hig[i]!=heights[i]:
                count += 1
                
        return count
        
