class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # Precompute palindrome table
        is_pal = [[False]*n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for i in range(n-1):
            is_pal[i][i+1] = (s[i] == s[i+1])
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_pal[i][j] = (s[i] == s[j]) and is_pal[i+1][j-1]

        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def min_cuts(i: int) -> int:
            if i == n or is_pal[i][n-1]:
                return 0
            
            min_cost = float('inf')
            for j in range(i, n):
                if is_pal[i][j]:
                    cost = 1 + min_cuts(j+1)
                    min_cost = min(min_cost, cost)
            return min_cost

        return min_cuts(0)
