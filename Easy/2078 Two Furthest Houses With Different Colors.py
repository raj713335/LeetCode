# https://leetcode.com/problems/two-furthest-houses-with-different-colors/


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        max_seperation = 0
        
        for i in range(0, len(colors)):
            for j in range(i+1, len(colors)):
                if colors[i] != colors[j]:
                    val = j-i
                    if val > max_seperation:
                        max_seperation = val
                        
        return max_seperation
        
