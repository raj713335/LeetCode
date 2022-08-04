# https://leetcode.com/problems/rotate-string/


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        s = list(s)
        goal = list(goal)
        
        n = len(s)
        
        while n > 0:
            if s == goal:
                return True
            else:
                s[:] = s[1:]+[s[0]]
                
            n -= 1
                
        return False
        
