# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        val = 0
        max_alt = 0
        
        for i in range(0, len(gain)):
            val += gain[i]
            if max_alt < val:
                max_alt = val
                
        return max_alt
        
