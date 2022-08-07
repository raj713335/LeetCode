# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        
        length = max(len(start), len(goal))
        
        start = ("0"*length + start)[-length:]
        goal = ("0"*length + goal)[-length:]
        
        count = 0
        
        for i in range(0, length):
            if start[i] != goal[i]:
                count += 1
                
        return count
        
