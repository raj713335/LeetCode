# https://leetcode.com/problems/shortest-distance-to-a-character/


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        output = []
        
        prev = s.index(c)
        
        for i in range(0, len(s)):
            if s[i] == c:
                prev = i
            temp = abs(prev - i)
            output.append(temp)
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                prev = i
            temp = abs(prev - i)
            if temp < output[i]:
                output[i] = temp   
                
        return (output)
        
