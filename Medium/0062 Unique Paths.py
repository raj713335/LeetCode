# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
        
        if (m,n) in memo:
            return memo[m,n]
        elif m==1 and n==1:
            return 1
        elif m==0 or n==0:
            return 0
        else:
            memo[m,n] = self.uniquePaths(m-1,n, memo) + self.uniquePaths(m, n-1, memo)
            
        return memo[m,n]
        
