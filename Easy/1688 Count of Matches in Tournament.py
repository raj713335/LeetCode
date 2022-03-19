# https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        matches = 0
        
        while (n != 1):
            if n%2==0:
                temp = n//2
                matches += temp
                n = temp
            else:
                temp = (n-1)//2
                matches += temp
                n = temp+1
        
        return matches
        
